"""Pure, inspectable policy and state-update components; no model/API calls."""
from dataclasses import dataclass, replace
from typing import Literal

Action = Literal["explain", "hinted_practice", "independent_practice", "transfer_challenge"]


@dataclass(frozen=True)
class Evidence:
    action: Action
    correct: bool
    used_hint: bool
    learner_id: str
    step: int


@dataclass(frozen=True)
class Belief:
    mastery: float = 0.25
    transfer: float = 0.15
    hint_dependency: float = 0.0
    count: int = 0


@dataclass(frozen=True)
class UpdateRule:
    """The learner-state update procedure, not merely a prompt or a tutor action."""
    success_gain: float = 0.13
    fail_penalty: float = 0.07
    hint_discount: float = 0.60
    transfer_bonus: float = 0.08
    dependence_gain: float = 0.08

    def validate(self) -> None:
        for key, value in vars(self).items():
            upper = 1.0 if key == "hint_discount" else 0.30
            if not 0 <= value <= upper:
                raise ValueError(f"out-of-bounds update rule: {key}={value}")

    def updated(self, **kwargs) -> "UpdateRule":
        rule = replace(self, **kwargs)
        rule.validate()
        return rule


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def update_belief(state: Belief, evidence: Evidence, rule: UpdateRule) -> Belief:
    rule.validate()
    multiplier = rule.hint_discount if evidence.used_hint else 1.0
    delta = rule.success_gain * multiplier if evidence.correct else -rule.fail_penalty
    transfer_delta = (
        (rule.transfer_bonus if evidence.correct else -rule.fail_penalty / 2)
        if evidence.action == "transfer_challenge" else 0
    )
    return Belief(
        mastery=clamp(state.mastery + delta),
        transfer=clamp(state.transfer + transfer_delta),
        hint_dependency=clamp(
            state.hint_dependency + rule.dependence_gain
            if evidence.used_hint else state.hint_dependency - 0.03
        ),
        count=state.count + 1,
    )


def choose_action(state: Belief, mode: str) -> Action:
    if mode == "static":
        return ("explain", "hinted_practice", "independent_practice", "transfer_challenge")[state.count % 4]
    if mode != "adaptive":
        raise ValueError(f"unknown tutoring mode: {mode}")
    if state.mastery < 0.34:
        return "explain" if state.count < 2 else "hinted_practice"
    if state.mastery < 0.58:
        return "hinted_practice" if state.hint_dependency < 0.25 else "independent_practice"
    if state.transfer < 0.53:
        return "transfer_challenge"
    return "independent_practice"
