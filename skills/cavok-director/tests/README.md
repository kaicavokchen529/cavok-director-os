# CAVOK Director Regression Tests

These tests protect directing quality as the Skill evolves. Run the same briefs after major rule changes and compare against the previous accepted version.

## Method

1. Use the test brief without adding hidden story facts.
2. Generate the requested director plan, not final video unless a model calibration is intended.
3. Score with `scorecard.md`.
4. Compare against the previous baseline.
5. A new rule must not improve one department by materially damaging unrelated departments.
6. Record regressions separately from model-specific generation failures.
7. For revision tests, verify that unrelated approved shots remain unchanged.
8. For reference-driven tests, verify that each reference affects only its assigned responsibility.
9. For continuity-heavy tests, verify visible posture/hand/contact transitions rather than only matching identity and screen direction.
10. For spatially complex tests, verify world-space consistency before evaluating lens or coverage.
11. For reference reconstruction, separate observed evidence from inference and new director design.
12. For calibration tests, lock already-correct dimensions before changing the failing layer.

## Core tests

01 dialogue; 02 boss reveal; 03 suspense discovery; 04 forest duel; 05 fire-vs-ice; 06 hyper-speed assault; 07 identity continuity; 08 long-take blocking; 09 daylight VFX; 10 aftermath; 11 spatial previs; 12 reference reconstruction/calibration; 13 skill isolation.

## Pass rule

No critical category may score below 3/5. Overall average target ≥4/5 for director-plan output. Any POV, causal-order or continuity violation is a critical failure regardless of average.