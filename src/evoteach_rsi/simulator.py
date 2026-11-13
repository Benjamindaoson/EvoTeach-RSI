"""Synthetic, explicitly non-human learner simulator for engineering tests only."""
from dataclasses import dataclass
import random
from statistics import mean
from .core import Belief, Evidence, UpdateRule, choose_action, update_belief, clamp


@dataclass(frozen=True)
class LearnerType:
    prior: float
    aptitude: float
    transfer_readiness: float
    cohort: str


@dataclass(frozen=True)
class Outcome:
    learner_id: str
    cohort: str
    learning_gain: float
    transfer: float
    retention: float
    hints: int
    objective: float
    evidence: tuple[Evidence, ...]


def learner_type(i: int) -> LearnerType:
    cohort = ("novice", "intermediate", "advanced")[i % 3]
    if cohort == "novice":
        return LearnerType(0.19, 0.70 + ((i * 7) % 11) / 40, 0.25, cohort)
    if cohort == "intermediate":
        return LearnerType(0.43, 0.75 + ((i * 7) % 11) / 40, 0.48, cohort)
    return LearnerType(0.64, 0.82 + ((i * 7) % 11) / 40, 0.68, cohort)


def simulate_one(learner_id: int, seed: int, rule: UpdateRule,
                 mode: str = "adaptive", steps: int = 12) -> Outcome:
    rng = random.Random(f"{seed}:{learner_id}")
    p = learner_type(learner_id)
    truth, transfer, independence = p.prior, max(0, p.prior - 0.13), 0.05
    belief = Belief(
        mastery=clamp(p.prior + rng.uniform(-0.09, 0.09)),
        transfer=max(0, p.prior - 0.13),
    )
    evidences = []
    hints = 0
    for step in range(steps):
        action = choose_action(belief, mode)
        if action == "explain":
            gain = (0.09 if truth < 0.48 else 0.04) * p.aptitude
        elif action == "hinted_practice":
            gain = (0.11 if truth < 0.65 else 0.05) * p.aptitude
            hints += 1
        elif action == "independent_practice":
            gain = (0.035 if truth < 0.32 else 0.105) * p.aptitude
            independence = clamp(independence + 0.11)
            transfer = clamp(transfer + 0.027 * p.aptitude)
        else:
            gain = (0.015 if truth < 0.46 else 0.085) * p.aptitude
            independence = clamp(independence + (0.015 if truth < 0.46 else 0.07))
            transfer = clamp(transfer + (0.01 if truth < 0.46 else 0.12) * p.aptitude * p.transfer_readiness)
        truth = clamp(truth + gain)
        probability = clamp(
            0.12 + 0.76 * truth
            + (0.14 if action == "hinted_practice" else 0)
            - (0.23 if action == "transfer_challenge" else 0)
        )
        correct = rng.random() < probability
        event = Evidence(action, correct, action == "hinted_practice", f"synthetic-{learner_id}", step)
        evidences.append(event)
        belief = update_belief(belief, event, rule)

    final_gain = truth - p.prior
    # Synthetic latent variables; NOT measured educational outcomes.
    retention = clamp(truth * (0.66 + 0.25 * independence))
    score = 0.38 * final_gain + 0.35 * transfer + 0.27 * retention - 0.005 * hints
    return Outcome(
        f"synthetic-{learner_id}", p.cohort, final_gain, transfer,
        retention, hints, score, tuple(evidences)
    )


def study(cohort_ids: range, seed: int, rule: UpdateRule,
          mode: str = "adaptive") -> list[Outcome]:
    return [simulate_one(i, seed, rule, mode) for i in cohort_ids]


def aggregate(outcomes: list[Outcome]) -> dict[str, float]:
    if not outcomes:
        raise ValueError("empty study")
    return {
        key: round(mean(getattr(outcome, key) for outcome in outcomes), 5)
        for key in ("learning_gain", "transfer", "retention", "hints", "objective")
    }
