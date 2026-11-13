# CS 6999 Master's Project — Research Proposal (Draft)

**Working title:** EvoTeach-RSI: Evidence-Gated Recursive Improvement of Pedagogical Agents

**Research context:** Proposed independent research for possible OMSCS CS 6999 supervision; no advisor acceptance, course approval, institutional affiliation for this repository, or research authorization is implied.

**Tentative period:** Spring–Fall 2027, subject to Georgia Tech requirements.

## Abstract

Educational AI tutors increasingly adjust their explanations, hints, and learning activities. However, the procedures by which tutors interpret learner evidence and improve their teaching policies are often fixed in advance. EvoTeach-RSI asks whether a pedagogical agent can **diagnose when its own teaching-improvement mechanism becomes unreliable**, propose bounded alternatives, and adopt a demonstrably better mechanism only after independent evaluation. We distinguish choosing the next pedagogical action from revising the algorithm that uses feedback to improve future actions. Programming education offers independently gradable tests, transfer tasks, and delayed retests. Our intended contribution is a reproducible research framework with interpretable update-rule representations, metacognitive failure diagnosis, matched-budget baseline comparisons, independent evaluation, and safety gates. v0.1 is a synthetic reference prototype only. Human learning claims require prospective, approved research.

## Research questions

- **RQ1 — Failure detection:** Can outcome evidence identify when and why a fixed teaching update rule becomes unreliable under changing student or task distributions?
- **RQ2 — Mechanism improvement:** Does evidence-gated rule revision improve held-out transfer and delayed retention compared with equally budgeted adaptive tutoring and first-order optimization?
- **RQ3 — Recursive scope:** Can modifying the candidate-generation or selection mechanism itself produce additional robust gains compared with equal-budget search?
- **RQ4 — Safeguards:** Which regression bounds, independent assessments, and teacher-approval gates prevent harmful updates and excessive reliance on hints?

## Hypotheses — to be tested

1. An interpretable, evidence-gated mechanism optimizer can outperform fixed-update adaptive tutoring on independent delayed-transfer tasks **under equal feedback and inference budgets**.
2. Explicitly accounting for uncertainty, hint dependence, and subgroup regressions can reduce harmful rule promotions.
3. Any gains attributable to *meta-rule changes*, rather than a larger search budget, will require separate held-out validation and ablation.

## Proposed method

1. Instrument verified learner events: attempts, hints, code tests, prerequisite evidence, transfer, independent success, delayed retests.
2. Define versioned, inspectable teaching-update operators. Initial bounded parameters discount hint-assisted success and weight independent transfer evidence.
3. Diagnose failures: inaccurate learner state, ineffective action policy, assessment leakage, or population shift.
4. Propose candidate changes to the update operator, not merely to explanations or prompts.
5. Run sandbox counterfactual evaluation on disjoint validation cohorts, with fixed budgets and predeclared promotion gates.
6. Evaluate on untouched students/tasks; report negative, null, and harmful outcomes alongside positive results.
7. With faculty and institutional approval, extend to prospective controlled education studies, pre/posttests, and delayed transfer.

## Baselines

| Arm | Mechanism |
|---|---|
| A0 | Static tutor schedule |
| A1 | Adaptive tutor with fixed learner update rule |
| A2 | Adaptive tutor plus retrieval of past teaching episodes |
| A3 | First-order threshold/weight tuning with equal optimization budget |
| A4 | Metacognitive update-rule revision and independent gate |
| A5 | Meta-level proposal/search-rule revision (exploratory only) |

All arms should share models, curriculum, tool access, feedback budget, and test secrecy. For a claim about recursion, A5 must outperform cost-matched A4 and random/grid search on held-out tasks.

## Measures

**Primary:** independent delayed retention and transfer on unseen problems. **Secondary:** skill gain, hint dependency, calibrated mastery estimates (ECE/Brier where appropriate), subgroup regression, teacher intervention, inference cost, and accepted/rejected proposal count. Use confidence intervals, transparent exclusion criteria, and preregistration when human evaluation is planned.

## Deliverables

- A clean open-source experimental harness with tests, versioned update operators and audit logs.
- A data contract and independent benchmark with strong baselines and ablation controls.
- A falsification-first experimental report, including failures and limits.
- A CS 6999 project report and, if warranted by results, a publication draft.

## Scope constraints

No new foundation-model training, no unreviewed student studies, no claim of open-ended self-improvement. The defensible Master's Project is **bounded, evidence-gated change to the pedagogical update rule**, tested against strong non-recursive baselines.

## Questions for a potential advisor

1. Is CS 6999 supervision for OMSCS students available in Spring 2027?
2. Could this connect to an existing machine-teaching, tutoring, or learner-modeling study?
3. Which learner outcomes and data sources are feasible within institutional policy?
4. What is the approval path for course registration, human data, and a three-semester research plan?
