# Safety, Student Data, and Governance

**Current v0.1:** Only synthetic learners and synthetic IDs. No student records or production credentials are needed or used.

## Before any human research

- Obtain faculty/institutional approval; determine IRB or other ethics review requirements before recruitment or data collection.
- Document informed consent, withdrawal/opt-out, data purposes, retention and deletion.
- Minimize events and pseudonymize learners. Limit raw data and model/API access by role.
- Never send private student submissions to outside model services without an approved basis.
- Do not use participation, grades or enrollment decisions as a reward target.
- Avoid using minors or vulnerable student populations without appropriate additional approvals.
- Keep teachers in charge of pedagogical boundaries and high-stakes decisions.

## Permitted autonomous changes

**Research sandbox:** bounded update-rule values, candidate-generation settings and reversible experimental configs.

**Never automatically change:** permissions, audit policy, consent rules, hidden answer keys, safety thresholds, external connectors, retention settings or arbitrary deployed code.

## Deployment gate — future only

1. Independent validation and equal-budget baselines.
2. Cohort-specific non-regression requirements and assessment-leakage checks.
3. Educator approval, logged justification and rollback version.
4. Limited pilot and ongoing drift/adverse-outcome monitoring.

Measure independent skill, transfer and delayed retention rather than maximizing engagement, satisfaction, or hint-dependent correct answers.
