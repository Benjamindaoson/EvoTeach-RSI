# EvoTeach-RSI

**Evidence-Gated Recursive Improvement for Educational Agents**

> **Status:** v0.1 research proposal + executable **synthetic** reference prototype. Not an evaluated educational product, not tested with actual students, and not evidence of general-purpose recursive self-improvement.

EvoTeach-RSI studies a harder question than selecting a better explanation: **Can a pedagogical agent recognize when its own learning-to-teach update mechanism fails, propose bounded alternatives, test them independently, and safely revise that mechanism?**

## Research objective

Separate three levels of change:

1. **Tutor behavior** — choose explanation, hinted practice, independent practice, or transfer assessment.
2. **Teaching improvement** — update learner-state estimates and teaching policies using observed evidence.
3. **Mechanism improvement** — inspect failures of the update operator itself, propose new rules, evaluate on separate synthetic cohorts, and promote or reject changes using regression guards.

```text
Learner actions and verified outcomes
      |
Evidence -> Learner Model -> Adaptive Tutor -> Teaching Action
      ^                                    |
      +--------------- feedback -----------+
                        |
         Metacognitive Failure Diagnosis
                        |
               Candidate Update Rules
                        |
       Sandbox / Paired Validation Cohorts
                        |
              Accept / Reject / Rollback
                        |
                Versioned Meta-Rule
```

## Implemented in v0.1

- Typed, deterministic learner evidence and a bounded learner-state `UpdateRule`.
- Four teaching actions and static versus adaptive tutor baselines.
- Seeded synthetic learner cohorts with simulated competence, transfer, and retention.
- A bounded candidate search over **update-rule parameters**, with subgroup regression checks.
- A basic meta-search-step adaptation, logging the accepted/rejected rule revisions.
- Distinct development cohorts and untouched final-test synthetic IDs.
- Reproducible JSON CLI experiment, seven regression/smoke tests, and GitHub Actions checks.

**Not implemented:** real LLM tutoring, validated human learning outcomes, production learner data, educator dashboards, real deployment safeguards, unrestricted self-modifying code, or a demonstration that RSI outperforms strong adaptive-learning baselines. The project is deliberately falsification-first.

## Install and reproduce

Requires Python 3.10+.

```bash
python -m pip install -e '.[test]'
python -m evoteach_rsi.cli --seed 2027 --generations 3 --output examples/synthetic_demo.json
pytest -q
```

`evoteach --seed 2027 --generations 3` is available as an installed command as well. All output metrics come from a **toy simulator**, not student studies.

## Evaluation principles

- Compare against matched static, adaptive, replay, and first-order optimization baselines.
- Hold feedback and compute budgets constant.
- Keep training, candidate selection, and final evaluation learners/tasks disjoint.
- Prioritize delayed retention, independent performance, and unseen-task transfer over chat satisfaction.
- Use cohort-specific non-inferiority gates; track failed edits and rollback.
- Obtain research ethics approval and educational oversight before any human-subject study.

## Documentation

- [CS 6999 research proposal](docs/CS6999_PROPOSAL_EN.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Experiment protocol](docs/EXPERIMENT_PROTOCOL.md)
- [Roadmap](docs/ROADMAP.md)
- [Related work and novelty boundaries](docs/RELATED_WORK.md)
- [Safety, privacy and data](docs/SAFETY_DATA.md)
- [Academic CV wording](docs/CV_POSITIONING.md)

## Context and scope

The research idea is relevant to metacognitive agents, machine teaching, learner modeling, adaptive expertise, and transfer. It is proposed as a potential Georgia Tech OMSCS CS 6999 project; **no faculty endorsement, university affiliation for this repository, ethics approval, or course registration is implied**.

Existing adjacent projects: [AI Talents Learning OS](https://github.com/Benjamindaoson/huisen-ai-adaptive-algorithm-coach) and [AI Agent Engineering Lab](https://github.com/Benjamindaoson/ai-agent-engineering-lab). Integration with those projects is **planned**, not implemented.

Relevant prior art includes [Kim, Islam & Goel (AAAI/IAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/41465) and other metacognitive-agent and intelligent-tutoring literature. Novelty and human impact are research questions, not established findings.

**Research principle:** Activity is not mastery; a better-looking synthetic metric is not evidence of better teaching in the real world.
