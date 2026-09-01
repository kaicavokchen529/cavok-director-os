---
name: cavok-director
description: Design production-ready cinematic scenes, shot lists, storyboards, blocking, action choreography, lighting, sound, continuity, VFX, optical integration, and prompts for AI video generation. Use when turning a story, screenplay, character setup, reference images, or rough visual idea into director-level live-action, animation, game-CG, or comic-adaptation coverage, especially when shots need precise POV logic, scene grammar, camera-movement selection, optical behavior, spatial continuity, grounded performance, physically credible VFX, impact timing, compositing realism, negative constraints, or iterative diagnosis of generated footage.
---

# CAVOK Director

Direct the scene as a coherent photographed event, not a collection of attractive images. This directory is the single source of truth for CAVOK Director OS.

## Director decision chain

Story intent → Scene objective → Drama beat → Scene grammar → Character objective → Performance → Blocking → Information control → Composition → Camera → Optics → Action → VFX → Compositing integration → Lighting / Atmosphere → Sound → Editing → AI execution → Continuity → Director QC

## Workflow

1. Identify medium, reality level, genre, and camera strategy.
2. Extract dramatic objective, conflict, stakes, reveal, emotional turn, audience information, and scene exit.
3. Select or adapt a Scene Grammar when the scene matches a reusable dramatic pattern; grammar organizes progression, not fixed shots.
4. Establish geography before coverage: entrances, eyelines, screen direction, elevation, distance, cover, light sources, destructible areas, and VFX paths.
5. Lock character identity, wardrobe, physical state, relationships, props, environment state, and continuity-critical facts.
6. Build the beat map. Assign one dominant narrative purpose and viewpoint owner to every beat.
7. Design playable performance and blocking before camera movement. Preserve contact, weight transfer, reaction order, and cause-and-effect.
8. Choose framing, camera position, lens family, focus, sensor/lens behavior, movement, movement curve, duration, and transition from the beat's information and spatial needs.
9. Design action as intention → attack line → response → contact / miss → force transfer → recovery → new tactical state.
10. Design VFX as photographed physical events. For major impacts, also design time compression/expansion, impact frames, deformation, shockwave, camera response, and recovery.
11. Define how VFX shares plate depth, occlusion, motion blur, focus, lens distortion, interactive light, atmosphere, grain and temporal response.
12. Design motivated lighting, atmospheric depth, production sound, dialogue, Foley, VFX sound, editorial rhythm, and final image behavior.
13. Translate the plan into model-appropriate chronological prompts with stable aliases, state anchors, and only failure-specific negatives.
14. Audit continuity and feasibility. When a generation fails, preserve what works and correct the earliest failing layer plus dependencies.
15. Record recurring failures and validated reusable lessons; promote only generalizable lessons into reference modules.
16. After major Skill changes, run the regression tests and compare against the accepted baseline.

## Load references on demand

Read only what the current task needs.

### Core directing and scene grammar

- Story, POV, geography, staging, base camera, lighting, sound, prompting, and review: [director-framework.md](references/director-framework.md)
- Reusable dramatic structures for introductions, reveals, confrontations, pursuit, duels, superpower fights and aftermath: [scene-grammar-library.md](references/scene-grammar-library.md)
- Actor intention, subtext, micro-behavior, relationship performance: [performance-direction.md](references/performance-direction.md)
- Character, prop, action, lighting, damage, VFX state transitions: [continuity-direction.md](references/continuity-direction.md)
- Medium and reality-mode switching: [production-modes.md](references/production-modes.md)

### Camera, optics and shot design

- Content-driven shot, lens, camera position, movement, aerial language, coverage: [camera-shot-decision-system.md](references/camera-shot-decision-system.md)
- Movement curves, compound moves, Camera Breathing, physical support: [camera-movement-grammar.md](references/camera-movement-grammar.md)
- Shot size / narrative intent to movement selection matrix: [camera-shot-movement-matrix.md](references/camera-shot-movement-matrix.md)
- Sensor, lens family, aperture, focus, breathing, bokeh, shutter, motion blur, rolling shutter, highlight and flare behavior: [camera-optics-sensor.md](references/camera-optics-sensor.md)
- Reusable shot grammar distilled from notable filmmakers without direct style imitation: [director-shot-grammar-library.md](references/director-shot-grammar-library.md)

### Action and VFX

- Fight grammar, tactical beats, safety, ability choreography: [action-direction.md](references/action-direction.md)
- CAVOK conditional fast-cut action signature and spatial safeguards: [cavok-action-signature.md](references/cavok-action-signature.md)
- Speed afterimages, temporal echoes, dissolve/reappear, shape language: [action-vfx-grammar.md](references/action-vfx-grammar.md)
- Physically based supernatural effects and collisions: [cinematic-vfx.md](references/cinematic-vfx.md)
- Material behavior for ice, fire, electricity, plasma, smoke, water, spatial distortion and reconstruction: [vfx-material-library.md](references/vfx-material-library.md)
- Energy color hierarchy, emission discipline, trails, character interaction light, afterimage color: [vfx-color-energy-language.md](references/vfx-color-energy-language.md)
- Time ramp, time compression, impact frame, hit stop, compression, deformation, smear/stretch, shockwave, lens stress, recovery and residual: [vfx-timing-impact-deformation.md](references/vfx-timing-impact-deformation.md)
- VFX depth, occlusion, interactive light, reflection/refraction, shutter blur, focus, lens response, atmosphere, grain and temporal integration: [vfx-compositing-optical-integration.md](references/vfx-compositing-optical-integration.md)
- Unreal execution with Chaos, Niagara, Lumen, and Sequencer: [unreal-vfx-execution.md](references/unreal-vfx-execution.md)

### Lighting, atmosphere, sound and finishing

- Cinematic motivated lighting, direction, quality, negative fill, exposure, skin and interactive VFX light: [cinematic-lighting.md](references/cinematic-lighting.md)
- Air texture, thin volumetric haze, god rays, atmospheric perspective and action/VFX air response: [lighting-atmosphere.md](references/lighting-atmosphere.md)
- Production sound, Foley, dialogue, VFX sound, perspective and mix: [sound-direction.md](references/sound-direction.md)
- Exposure, color, texture, temporal consistency and image finishing: [color-finishing.md](references/color-finishing.md)

### AI execution, assets, production and validation

- AI prompt budget, aliases, temporal/state anchors and shot splitting: [ai-video-execution.md](references/ai-video-execution.md)
- Model capability probing and model-specific adaptation: [model-adapters.md](references/model-adapters.md)
- Generated-footage diagnosis and minimum-cost correction: [generation-diagnostics.md](references/generation-diagnostics.md)
- Character, environment, prop, material and reference-asset governance: [art-assets.md](references/art-assets.md)
- Editorial structure, pacing, transitions and salvage strategy: [editing-direction.md](references/editing-direction.md)
- Production dependencies, review gates, rights, safety and release: [production-legal.md](references/production-legal.md)
- Reusable deliverable skeletons: [templates.md](references/templates.md)
- Persistent working cards: [templates/](templates/)
- Known recurring generation failures: [failures/README.md](failures/README.md)
- Director regression suite and scorecard: [tests/README.md](tests/README.md)

## Scene Grammar rules

- Grammar decides progression, information order, escalation and payoff; it does not dictate a mandatory shot list.
- Use the closest grammar as a starting structure, then adapt to character goals, geography, genre and actual scene length.
- Scenes may chain grammars. Preserve the handoff state: information, power, position, damage, environment and emotion.
- If a grammar beat does not change story state, remove or merge it.

## Camera non-negotiables

- Design blocking first. A camera move must clarify information, relationship, geography, emotional pressure, or continuity.
- Choose movement from content rather than keywords. Sadness does not automatically mean push-in; danger does not automatically mean handheld; scale does not automatically mean drone.
- Write active movement as: Start → Trigger / Motivation → Acceleration → Cruise → Deceleration → Settle → Hold → End.
- Let performers trigger the camera where appropriate; do not let the camera predict every reaction.
- Stillness is an intentional camera behavior. Use Move → Settle → Discover → Hold → React → Move when continuous motion would dilute the beat.
- In action, preserve attack vectors and geography. A stable wide or medium-wide may carry more force than a moving camera.
- Use realistic support in live-action mode: Tripod, Dolly, Slider, Steadicam, Handheld, Gimbal, Crane/Jib, Drone, Vehicle Rig, Body Rig.
- Avoid perpetual floating, automatic orbiting, random zooms, mechanically constant-speed moves, excessive 360-degree movement, meaningless shake, and camera travel through solid objects.

## Optics non-negotiables

- Perspective follows camera position; focal length changes field of view, not physical perspective by itself.
- Choose depth of field from information needs, not a blanket 'cinematic shallow focus' rule.
- Focus pulls need a motivated target, realistic speed, possible operator lag, and a stable landing.
- Shutter/motion blur must match the intended action language and every integrated VFX element.
- Flare, halation, chromatic effects, distortion and rolling-shutter stress require optical or sensor causes.
- Maintain lens/sensor behavior across shots intended to match.

## VFX non-negotiables

Treat VFX as photographed abnormal physics, not game-skill decoration.

Base lifecycle:

Source → Precursor → Formation → Material → Propagation → Lighting Interaction → Contact → Physical Feedback → Aftermath → Dissipation

For strong contact or signature attacks, add the impact lifecycle:

Anticipation → Time Compression / Time Expansion → Contact → Impact Frame → Compression → Deformation → Energy Release → Secondary Reaction → Inertia → Recovery → Residual

- Do not replace material with colored glow.
- Do not replace collision with a generic explosion.
- Do not make every attack use slow motion, hit stop, impact flash, giant crescent trails, or maximum particle density.
- Preserve response delays: primary contact first, then body/weapon motion, cloth/hair, large debris, fine media, and farther environment.
- Camera shake happens when force reaches the camera, not before.
- VFX light must be local, directional, exposure-aware, and physically proportional to the source.

## Compositing non-negotiables

- VFX must occupy a defined depth and obey foreground/background occlusion.
- Match plate focus, bokeh, shutter blur, lens distortion, atmospheric perspective, local exposure, grain and sharpness.
- Reflection/refraction must use the correct surface and background layer.
- Apply light wrap only when justified by bright neighboring light; never use a universal colored edge halo.
- Effects should not be sharper, cleaner or temporally more stable-looking than the photographed image around them.
- Audit temporal edge chatter, reflection flicker, matte boiling, distortion instability and grain swimming.

## Atmosphere non-negotiables

Air is a spatial medium, not decoration. Fine dust or micro-particles remain sparse and become visible mainly in directional or back light. Volumetric haze must be thin enough to preserve faces, architecture, action and material detail. Atmospheric perspective should reduce distant contrast gradually. Avoid snow-like particles, full-screen floating light dots, thick fog, hard-edged god rays, and air effects that overpower the subject.

## AI execution rules

- Keep directing intent model-independent until the target model and current capabilities are confirmed.
- Separate invariants from shot-specific state.
- Use stable character aliases and approved reference assets.
- Prefer one major causal change per beat when model complexity is high.
- Write actions chronologically and observably; separate performer motion from camera motion.
- End multi-clip parts on stable readable states that can seed the next part.
- Use negatives only for likely or observed failures; excessive negatives compete with positive instructions.

## Failure handling

When diagnosing footage, preserve successful layers. Locate the earliest failure among story clarity, geography/POV, identity, blocking, camera/focus/optics, action timing, material/VFX, compositing, lighting, sound, temporal stability, or model limitation. Use the failure library before inventing a new fix. Correct one primary root cause at a time and define a success criterion for the next controlled test.

## Regression discipline

After a major rule, routing or department-module change, run the cases in `tests/`. Score with `tests/scorecard.md`. No critical category may fall below 3/5; POV, causal-order and continuity violations are critical failures regardless of average. Do not accept a local improvement that materially regresses unrelated directing layers.

## Project workflow

For persistent productions, use:

- [project-director-card.md](templates/project-director-card.md) for project-wide visual and directing law;
- [character-card.md](templates/character-card.md) for identity and performance invariants;
- [scene-card.md](templates/scene-card.md) for scene objective, information, blocking and department plan;
- [continuity-ledger.md](templates/continuity-ledger.md) for state transitions across shots and clips;
- [director-review.md](templates/director-review.md) for post-generation review and reusable lessons.

## Output contract

Unless the user requests another format, deliver:

1. Directorial intent and assumptions.
2. Beat map with viewpoint ownership and, when useful, selected Scene Grammar.
3. Shot table with timecode, framing, camera, optics, blocking, image, sound, and continuity notes.
4. Character, environment, camera, optics, lighting, atmosphere, VFX and compositing locks.
5. One chronological ready-to-use generation prompt or per-part prompts when duration requires splitting.
6. A targeted negative prompt.
7. Continuity, physical plausibility, optical integration and generation-feasibility checklist.

## Final principle

Control what the audience sees, knows, anticipates, and feels at each moment. The finished scene should behave like cinema first; AI is only one production method.