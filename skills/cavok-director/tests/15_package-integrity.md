# Test 15 — Package Integrity

## Brief

Audit the CAVOK Skill after a rule or module change. Confirm that the package remains self-contained, its relative routes resolve, its root instructions stay concise, and newly learned mechanisms have one CAVOK authority rather than duplicated definitions.

## Requirements

- Run `scripts/validate_skill.py` from the Skill package.
- Require only `name` and `description` in frontmatter.
- Require `SKILL.md` to remain within its line budget.
- Reject dangling relative links and links escaping the package.
- Reject machine-specific absolute paths and known external-system identifiers in Markdown.
- Reject byte-identical Markdown duplicates.
- Confirm the combat decision engine, cinematography language engine, action–VFX–camera orchestration, rule authority map, and isolation contract remain routed from `SKILL.md`.
- Confirm the camera-language contract still distinguishes seven camera dimensions, crash-in from crash zoom, pull-out from zoom-out, overhead angle from elevation movement, and bullet time from ordinary slow motion.
- Confirm the orchestration contract still treats action/VFX/camera/shot-size matrices as candidates, preserves a no-added-VFX option, and covers physical actions, supernatural actions, camera-vector relations, contact classes and shot-size selection.
- Confirm model adapters alter execution syntax only, not directing logic.

## Critical Failures

- Validation returns a nonzero exit status.
- A rule depends on hidden chat state, an unrelated Skill, or an unlisted file.
- The same normative rule is independently defined in competing modules.
- External project material appears in the package as CAVOK source truth.
