# Falsification-first Experiment Protocol

## Primary question

Does improving the **rule that updates teaching behavior from feedback** yield higher *independent delayed transfer and retention* than strong adaptive-tutoring baselines at an equal search, model, data and tool budget?

**Null is a legitimate result.** Stronger claims require stronger independent evidence.

## Stage 0 — Synthetic engineering harness (implemented)

- Seeded heterogeneous toy learners across novice/intermediate/advanced profiles.
- Twelve teaching interactions per learner.
- Action space: explain, hinted practice, independent practice, transfer challenge.
- Aggregate synthetic latent outcomes: learning gain, transfer, retention, hints, composite score.
- Candidate parameter updates proposed on per-generation validation learner IDs.
- Final synthetic learner IDs 90000–90299 excluded from candidate selection.

These are hand-specified toy dynamics. They are for regression tests, not validated educational science.

## Stage 1 — Replay and benchmark (planned)

- Obtain authorized, properly licensed interaction traces or expert-created assignments.
- Keep learner IDs, task templates, curriculum units and assessment rubrics disjoint across splits.
- Use independent graders and hidden answers. The tutor and meta-agent cannot access final-test keys.
- Evaluate novel skill units, contradictory evidence, hint-seeking behavior, and population shifts.

## Stage 2 — Prospective human evaluation (planned; requires approvals)

- Obtain advisor/institutional permission and determine IRB/ethics requirements **before** recruitment.
- Establish informed consent, adult participant eligibility, attrition/missingness plan and data retention limits.
- Pretest → controlled learning interval → posttest → delayed retest and transfer problems.
- Random assignment at learner or cohort level with educator oversight and opt-out.
- Report confidence intervals, actual sample sizes, exclusions, adverse effects and null results.

## Predeclared comparison arms

| Arm | What changes? |
|---|---|
| A0 Fixed sequence | Nothing |
| A1 Fixed-rule adaptive tutor | Immediate teaching actions |
| A2 Episodic experience tutor | Teaching actions + retrieved cases |
| A3 Cost-matched policy tuning | Parameters or thresholds within fixed algorithm |
| A4 Meta-gated update-rule revision | Evidence-to-state/policy update operator |
| A5 Recursive meta-rule revision | Proposal generator or selection mechanism (exploratory) |

Do not credit A4 with gains attributable to more data, more tokens, repeated exposure to the final test, or weaker baselines.

## Evaluation metrics

1. **Primary:** unseen-task transfer and delayed independent retention.
2. **Learning evidence:** pre/post improvement, independently executed tasks, meaningful code tests.
3. **Calibration:** ECE, Brier score or proper scoring rules where the probabilistic contract supports them.
4. **Harm:** novice/cohort regression, hint dependency, accessibility and educator vetoes.
5. **Efficiency:** performance per attempt, per instructor hour, token and compute budget.
6. **Meta contribution:** A5–A4 gap with matching candidate count, training exposure and feedback budget.

## Ablations

- Remove failure attribution.
- Remove independence/transfer evidence from reward.
- Remove holdout promotion gate.
- Remove cohort-specific regression protection.
- Freeze proposal-search step size.
- Replace meta search with random/grid search under matched budget.

## Failure / stopping rules

- If A4 ≤ A3 on locked primary metrics, do not claim a mechanism-improvement advantage.
- If A5 fails to beat matched A4, do not claim recursive mechanism-level benefit.
- If improvements vanish on new curriculum units, restrict claims to observed domain.
- If subgroup harm exceeds predeclared margin, reject promotion irrespective of mean score.
- If leakage/contamination is found, invalidate affected tests.
- If evaluation samples are insufficient, report uncertainty instead of promising publication.

## Reproducibility

Record code commit, config and dataset hashes, simulator version, random seed, model ID, inference budget, split definitions, baseline implementation, candidate proposals, decisions and rejected revisions. Preserve a never-touched final-test set.
