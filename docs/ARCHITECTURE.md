# Architecture & Contracts

This is the **target architecture**. The Python v0.1 implementation is a small synthetic reference; do not confuse these proposed modules with deployed components.

## Layers

| Layer | Role | Outputs | Boundary |
|---|---|---|---|
| L0 Evidence | Collect verified attempts and assessment outcomes | append-only `EvidenceEvent` | consent, retention, access control |
| L1 Tutor | Learner state, skill graph, explanation/practice policy | teaching action, trace | hidden answers inaccessible |
| L2 Improvement | Diagnose errors; update learner/pedagogy state | candidate `UpdateRule` | sandbox-only writes |
| L3 Meta-improvement | Diagnose failures in L2 and propose revision strategies | versioned `MetaRule` | held-out evaluation |
| Governance | Independent gate and educator approval | approve/reject/rollback | never self-edit safety settings |

## Versioned future contracts

- `EvidenceEvent`: event ID, pseudonymous learner ID, skill ID, assessment ID, action, verified outcome, hint use, timestamp, provenance, consent scope.
- `LearnerState`: mastery, uncertainty, misconception tags, transfer/retention estimate, hint dependency, evidence IDs, estimator version.
- `TeachingPolicy`: version, allowable actions, curriculum constraints, decision parameters, budget, safety policy.
- `UpdateRule`: evidence weights, state transition operator, confidence model, version, interpretable diff.
- `MetaRule`: search budget, proposal strategy, validation rules, subgroup thresholds, version.
- `RuleChangeProposal`: incumbent/candidate IDs, failure evidence, causal hypothesis, risk, expected effect and rollback handle.
- `EvaluationRecord`: locked split hashes, metrics, uncertainty, cohort deltas, compute budget, accept/reject rationale.

## Decision and improvement path

```text
Verified learner event → LearnerState → TeachingPolicy → Tutor action
        ↑                                           |
        +---------------- assessed outcome ---------+
                             |
                   Failure attribution
                             |
                   Candidate UpdateRule
                             |
         Sandbox paired evaluation on held-out cohorts
                             |
              Independent safety / utility gate
                             |
            Reject / educator approval / rollback
                             |
              Version history and audit trail
```

## Current v0.1 package mapping

- `core.py`: `Evidence`, `Belief`, `UpdateRule`, `update_belief`, `choose_action`.
- `simulator.py`: deterministic toy student heterogeneity, actions, feedback, simulated transfer/retention.
- `evolution.py`: bounded candidate rule search, three-cohort regression guard, adapted proposal step size.
- `cli.py`: validation-only rule selection and independent final synthetic IDs.
- `tests/`: deterministic execution, rule bounds, cohort guard and output contracts.

The final-test synthetic cohort cannot justify real-world learning claims. Updating the proposal step size is an engineering example of meta-adaptation, **not evidence of full recursive self-improvement**.

## Intended external integrations — not yet implemented

- AI Talents Learning OS verified learning events and skill graph.
- AI Agent Engineering Lab independent code tasks and sandbox grading.
- Educator-approved RAG tutor through a version-pinned model interface.
- Optional typed APIs, PostgreSQL store, experiment registry, and educator review UI.

## Formal abstraction

Let `s_t` be learner state, `e_t` verified feedback, `π` the teaching policy, `U_φ` the learner/teaching update operator, and `M_ψ` the mechanism for improving `U`.

```text
action(t)       = π(state(t), skill(t))
state(t+1)     = U_φ(state(t), evidence(t))
φ(t+1)         = M_ψ(φ(t), history, validation_evidence)
ψ(t+1)         = MetaRevision(ψ(t), meta_validation_evidence)
```

A genuinely recursive claim requires isolating improvement from the last line under equal compute and feedback; merely changing `φ` does not establish this.
