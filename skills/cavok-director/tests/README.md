# CAVOK Director Regression Tests

These tests protect directing quality as the Skill evolves. Run the same briefs after major rule changes and compare against the previous accepted version.

## Method

1. Use the test brief without adding hidden story facts.
2. Generate the requested director plan, not final video unless a model calibration is intended.
3. Score with `scorecard.md`.
4. Compare against the previous baseline.
5. A new rule must not improve one department by materially damaging unrelated departments.
6. Record regressions separately from model-specific generation failures.

## Core tests

01 dialogue; 02 boss reveal; 03 suspense discovery; 04 forest duel; 05 fire-vs-ice; 06 hyper-speed assault; 07 identity continuity; 08 long-take blocking; 09 daylight VFX; 10 aftermath.

## Pass rule

No critical category may score below 3/5. Overall average target ≥4/5 for director-plan output. Any POV, causal-order or continuity violation is a critical failure regardless of average.