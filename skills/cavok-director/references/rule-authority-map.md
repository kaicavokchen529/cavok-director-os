# Rule Authority Map

## Purpose

Use this map when two CAVOK files appear to govern the same decision. Keep one normative definition per concept; other files may route to it or explain downstream application without redefining it.

## Precedence

1. Active user request and explicit approved project locks.
2. `isolation-contract.md` for source boundaries and conflict handling.
3. The domain authority listed below.
4. Conditional medium, model, platform, and production adapters.
5. Templates, tests, failure examples, and previous outputs, which are non-normative evidence.

When two domain authorities overlap, preserve both responsibilities and resolve the decision at the earliest causal layer. Do not copy a rule into a second file to settle the conflict.

## Domain authorities

| Decision | Normative authority | Downstream consumers |
|---|---|---|
| Overall directing chain, POV, beat purpose, base staging | `director-framework.md` | scene grammars, camera, performance |
| Evidence states, readiness, spatial previs, calibration | `production-previs-evidence-gates.md` | all departments |
| Medium and reality-mode routing | `production-modes.md` | hyperreal and 2D action modules |
| Tactical combat legality, fighter state, adaptation, action value | `combat-decision-engine.md` | action, camera, continuity, AI adapters |
| Hyperreal performer-camera coupling and 3D action staging | `hyperreal-action-direction-v2.md` | shot design, AI execution |
| 2D/anime pose, timing, spacing, deformation and FX grammar | `2d-anime-combat-grammar.md` | shot design, model adapter |
| Cross-shot body, prop, damage, momentum and environment state | `continuity-direction.md` | templates, AI execution |
| Scene camera language, viewpoint arc, visual-distance curve, support/optical palette, expressive candidates and platform handoffs | `cinematography-language-engine.md` | shot, movement, optics, medium and model modules |
| Shot framing and world-space camera position | `camera-shot-decision-system.md` | optics, movement grammar |
| Camera movement curves and support behavior | `camera-movement-grammar.md` | hyperreal action, shot plans |
| Optical and sensor behavior | `camera-optics-sensor.md` | compositing, AI prompts |
| VFX causality and supernatural collisions | `cinematic-vfx.md` | material, timing and compositing modules |
| VFX timing, impact and deformation | `vfx-timing-impact-deformation.md` | action and compositing |
| VFX optical integration | `vfx-compositing-optical-integration.md` | final shot and QC |
| Lighting source and exposure logic | `cinematic-lighting.md` | atmosphere, VFX, finishing |
| Atmosphere and volumetric behavior | `lighting-atmosphere.md` | lighting, compositing |
| Sound cause, perspective and dynamics | `sound-direction.md` | editing, continuity |
| AI prompt structure, complexity and segmentation | `ai-video-execution.md` | model adapters |
| Model-specific syntax and capability limits | the selected adapter only | final prompt |
| Isolation, external references and historical context | `isolation-contract.md` | all modules |

## Change discipline

- Change the authority file first.
- Replace duplicate definitions elsewhere with a direct pointer.
- Keep hard constraints separate from heuristics and examples.
- Treat numerical guidance as context-dependent unless a production or platform adapter makes it a verified hard limit.
- Delete superseded wording instead of preserving competing old and new rules.
- Run `scripts/validate_skill.py` after changes.
