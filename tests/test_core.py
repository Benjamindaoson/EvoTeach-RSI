import pytest
from evoteach_rsi.core import Belief, Evidence, UpdateRule, choose_action, update_belief
from evoteach_rsi.evolution import MetaRule, compare, evolve
from evoteach_rsi.simulator import simulate_one, study, aggregate


def test_evidence_state_updates():
    evidence = Evidence("hinted_practice", True, True, "synthetic-1", 0)
    state = update_belief(Belief(), evidence, UpdateRule())
    assert state.count == 1
    assert state.mastery > 0.25
    assert state.hint_dependency > 0


def test_rule_bounds():
    with pytest.raises(ValueError):
        UpdateRule().updated(hint_discount=1.4)


def test_synthetic_determinism():
    a = simulate_one(5, 91, UpdateRule())
    b = simulate_one(5, 91, UpdateRule())
    assert a == b
    assert len(a.evidence) == 12
    assert a.learner_id.startswith("synthetic-")


def test_policy_returns_valid_action():
    assert choose_action(Belief(), "static") in (
        "explain", "hinted_practice", "independent_practice", "transfer_challenge"
    )


def test_evolution_bounded_and_reproducible():
    a = evolve(UpdateRule(), generations=2)
    b = evolve(UpdateRule(), generations=2)
    assert a == b
    assert a[1].generation == 2
    a[0].validate()


def test_guard_rejects_unacceptable_cohort_regression():
    baseline = UpdateRule()
    candidate = baseline.updated(success_gain=0.01)
    result = compare(candidate, baseline, range(1000, 1090), 2027, MetaRule(min_gain=1.0))
    assert not result["accepted"]


def test_summary_metrics():
    summary = aggregate(study(range(12), 10, UpdateRule()))
    assert set(summary) == {"learning_gain", "transfer", "retention", "hints", "objective"}
