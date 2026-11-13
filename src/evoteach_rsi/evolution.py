"""Bounded rule search, separate validation cohorts, and meta-rule versioning."""
from dataclasses import dataclass, replace
from .core import UpdateRule
from .simulator import aggregate, study


@dataclass(frozen=True)
class MetaRule:
    """How to propose and accept changes to the learner-state update procedure."""
    step_size: float = 0.035
    min_gain: float = 0.001
    max_group_regression: float = 0.006
    generation: int = 0


def candidate_rules(current: UpdateRule, meta: MetaRule) -> list[UpdateRule]:
    candidates = []
    for key in ("success_gain", "fail_penalty", "hint_discount",
                "transfer_bonus", "dependence_gain"):
        for sign in (-1, 1):
            value = getattr(current, key) + sign * meta.step_size
            try:
                candidates.append(current.updated(**{key: round(value, 5)}))
            except ValueError:
                pass
    return candidates


def cohort_scores(rule: UpdateRule, ids: range, seed: int) -> dict[str, float]:
    outcomes = study(ids, seed, rule)
    return {
        cohort: aggregate([outcome for outcome in outcomes if outcome.cohort == cohort])["objective"]
        for cohort in ("novice", "intermediate", "advanced")
    }


def compare(candidate: UpdateRule, incumbent: UpdateRule, ids: range,
            seed: int, meta: MetaRule) -> dict:
    candidate_score = aggregate(study(ids, seed, candidate))["objective"]
    incumbent_score = aggregate(study(ids, seed, incumbent))["objective"]
    candidate_groups = cohort_scores(candidate, ids, seed)
    incumbent_groups = cohort_scores(incumbent, ids, seed)
    worst = min(candidate_groups[key] - incumbent_groups[key] for key in candidate_groups)
    gain = candidate_score - incumbent_score
    return {
        "candidate": candidate,
        "delta": round(gain, 6),
        "worst_cohort_delta": round(worst, 6),
        "accepted": gain >= meta.min_gain and worst >= -meta.max_group_regression,
    }


def evolve(initial: UpdateRule, generations: int = 3,
           seed: int = 2027) -> tuple[UpdateRule, MetaRule, list[dict]]:
    """Candidate selection uses validation IDs; separate final-test IDs are untouched."""
    if generations < 0:
        raise ValueError("generations must be nonnegative")
    rule, meta, log = initial, MetaRule(), []
    for g in range(generations):
        dev_ids = range(1000 + 120 * g, 1090 + 120 * g)
        results = [
            compare(candidate, rule, dev_ids, seed + g, meta)
            for candidate in candidate_rules(rule, meta)
        ]
        best = max(results, key=lambda item: item["delta"], default=None)
        changed = bool(best and best["accepted"])
        if changed:
            rule = best["candidate"]
        log.append({
            "generation": g + 1,
            "accepted": changed,
            "gain": best["delta"] if best else 0,
            "worst_cohort_delta": best["worst_cohort_delta"] if best else 0,
            "meta_rule_before": vars(meta),
            "rule_after": vars(rule),
        })
        # This is constrained step-size adaptation, NOT proof of broad RSI.
        step = meta.step_size * (1.08 if changed else 0.65)
        meta = replace(meta, step_size=round(max(0.005, min(0.07, step)), 5), generation=g + 1)
    return rule, meta, log
