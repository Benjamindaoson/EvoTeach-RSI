# Research Roadmap — v0.1 to a Defensible CS 6999 Study

This is a proposed development plan, **not** an approved Georgia Tech course schedule.

## Milestone 0 — Working research reference (v0.1)

- [x] Deterministic synthetic simulator with heterogeneous learners.
- [x] Static and fixed-adaptive tutor policies.
- [x] Typed learner evidence and bounded update parameters.
- [x] Candidate rule search with cohort regression gate.
- [x] Basic meta-search step-size versioning.
- [x] Separate synthetic development and final cohorts.
- [x] CLI, reproducible JSON output, seven tests and CI.
- [ ] Evidence for improved outcomes with real learners.

## Milestone 1 — Scientific validity

- [ ] Formal taxonomy of learner-model failures vs teaching-policy failures.
- [ ] Strong equal-budget A2 and A3 baselines, random/grid search.
- [ ] Immutable split manifests, task leakage tests and multi-seed uncertainty.
- [ ] Failure cases where changing update rules causes measurable harm.
- [ ] Predeclared non-inferiority thresholds and hard stop criteria.

## Milestone 2 — Realistic educational tasks

- [ ] Create educator-reviewed RAG/coding lessons and hidden independent tests.
- [ ] Integrate consent-compliant practice events via explicit adapter.
- [ ] Test delayed transfer/retention rather than answer helpfulness.
- [ ] Add curriculum population shift and novice/advanced subgroups.
- [ ] Separate teacher system/model quality from optimization-method quality.

## Milestone 3 — Mechanism-level causal evidence

- [ ] Attribute sustained learning failures to update-operator components.
- [ ] Compare bounded revisions against first-order weight tuning.
- [ ] Test meta-proposal changes under fixed feedback/search budget.
- [ ] Ablate proposal mechanism and promotion/safety gates independently.
- [ ] Release a paper-ready, reproducible experiment bundle including negative results.

## Milestone 4 — Educator-in-the-loop research system

- [ ] Versioned experiment registry with append-only audit history.
- [ ] Review UI for educator approval, rejection and rollback.
- [ ] Institution-approved study protocol before any student deployment.
- [ ] Monitoring for harms, drift, hint dependency and subgroup regression.

## Suggested three-semester plan (subject to formal approval)

| Semester | Focus | Exit artifact |
|---|---|---|
| Spring 2027 | Baselines, learner evidence, failure diagnosis | research protocol and reproducible benchmark |
| Summer 2027 | Update-rule revision, independent gates, ablations | experimental method and validation results |
| Fall 2027 | Robustness, meta-evaluation, report | CS 6999 report and conditional manuscript draft |

## Scope limits

**Must:** narrow skill family, clear update operator, matched baseline, locked holdouts and controlled ablations.

**Optional:** production dashboard, real-time LLM sessions, integration with other learning products.

**Out of scope for Master's Project:** training a foundation model, unrestricted code rewriting, broad general AGI claims, unauthorized student experiments.

## Risks

| Risk | Mitigation |
|---|---|
| Toy environment flatters one strategy | external benchmarks, changed simulators, strong baselines |
| Meta-search overfits | immutable final test, budget-matched A4/A5 |
| Faculty fit unclear | offer integration with existing DILab teaching studies |
| No permission for student data | stay with public/replay/synthetic analyses |
| Project too broad | reduce to one skill family and one update operator |
