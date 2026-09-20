---
name: cavok-director
description: Design production-ready cinematic scenes, shot lists, storyboards, blocking, action choreography, lighting, sound, continuity, VFX, optical integration, and prompts for AI video generation. Use when turning a story, screenplay, character setup, reference images, or rough visual idea into director-level live-action, animation, game-CG, or comic-adaptation coverage, especially when shots need precise POV logic, scene grammar, camera-movement selection, optical behavior, spatial continuity, grounded performance, physically credible VFX, impact timing, compositing realism, negative constraints, or iterative diagnosis of generated footage.
---

# CAVOK Director

Direct the scene as a coherent photographed or deliberately animated event, not a collection of attractive images. This directory is the single source of truth for CAVOK Director OS.

## Director decision chain

Story intent → Scene objective → Drama beat → Scene grammar → Character objective → Performance → Blocking → Information control → Composition → Camera → Optics / Graphic timing → Action → VFX / FX drawing → Compositing integration when applicable → Lighting / Atmosphere → Sound → Editing → AI execution → Continuity → Director QC

## Workflow

1. Identify medium, reality level, genre, and camera strategy.
2. Extract dramatic objective, conflict, stakes, reveal, emotional turn, audience information, and scene exit.
3. Select or adapt a Scene Grammar when the scene matches a reusable dramatic pattern; grammar organizes progression, not fixed shots.
4. Establish geography before coverage: entrances, eyelines, screen direction, elevation, distance, cover, light sources, destructible areas, and VFX paths.
5. Lock character identity, wardrobe, physical state, relationships, props, environment state, continuity-critical facts, approved decisions, and reference responsibilities.
6. If the user is revising existing work, define revision scope before redesign: what is locked, what is editable, and what dependencies may change. Preserve approved material outside that scope.
7. Build the beat map. Assign one dominant narrative purpose and viewpoint owner to every beat.
8. Design playable performance and blocking before camera movement. Preserve contact, weight transfer, reaction order, and cause-and-effect. In hyperreal combat, treat performance tell, action vector, three-dimensional staging, and camera response as a coupled system. In 2D/anime action, also protect key-pose readability, silhouette, timing, spacing, deformation and consequence pose.
9. Choose framing, camera position, lens family or graphic perspective, focus when applicable, movement, movement curve, duration, and transition from the beat's information and spatial needs. For hyperreal combat, every conspicuous camera move must have a performer, force, spatial, or information trigger.
10. Design action as intention → attack line → response → contact / miss → force transfer → recovery → new tactical state. In hyperreal combat, extend this into performance tell → load → 3D action vector → camera trigger → action burst → camera choreography → contact → consequence → settle. In 2D/anime combat, translate it into Read Pose → Anticipation → Launch → Burst/Smear → Contact → Consequence Pose → Recovery.
11. Design VFX or hand-drawn FX as causal events. For major impacts, also design time compression/expansion, impact frames, deformation, shockwave or graphic force lines, camera/graphic response, and recovery.
12. In photographed or hybrid modes, define how VFX shares plate depth, occlusion, motion blur, focus, lens distortion, interactive light, atmosphere, grain and temporal response. In 2D/anime mode, define line hierarchy, background state, smear, impact tier and FX lifecycle instead.
13. Design motivated lighting, atmospheric depth, production sound, dialogue, Foley, VFX/FX sound, editorial rhythm, and final image behavior.
14. Translate the plan into model-appropriate chronological prompts with stable aliases, state anchors, and only failure-specific negatives.
15. Audit continuity and feasibility. When a generation fails, preserve what works and correct the earliest failing layer plus dependencies.
16. Record recurring failures and validated reusable lessons; promote only generalizable lessons into reference modules.
17. After major Skill changes, run the regression tests and compare against the accepted baseline.

## Load references on demand

Read only what the current task needs.

### Core directing and scene grammar

- Story, POV, geography, staging, base camera, lighting, sound, prompting, and review: [director-framework.md](references/director-framework.md)
- Reusable dramatic structures for introductions, reveals, confrontations, pursuit, duels, superpower fights and aftermath: [scene-grammar-library.md](references/scene-grammar-library.md)
- Actor intention, subtext, micro-behavior, relationship performance: [performance-direction.md](references/performance-direction.md)
- Character, prop, action, lighting, damage, VFX state transitions: [continuity-direction.md](references/continuity-direction.md)
- Medium and reality-mode switching, including routing into hyperreal and 2D/anime combat grammar: [production-modes.md](references/production-modes.md)

### Camera, optics and shot design

- Content-driven shot, lens, camera position, movement, aerial language, coverage: [camera-shot-decision-system.md](references/camera-shot-decision-system.md)
- Movement curves, compound moves, Camera Breathing, physical support, action-camera coupling and showmanship: [camera-movement-grammar.md](references/camera-movement-grammar.md)
- Hyperreal / live-action-feeling combat direction: performance-triggered camera movement, 3D action staging, camera choreography, camera stunt grammar, hero moves, character camera signatures and anti-flatness QC: [hyperreal-action-direction-v2.md](references/hyperreal-action-direction-v2.md)
- Shot size / narrative intent to movement selection matrix: [camera-shot-movement-matrix.md](references/camera-shot-movement-matrix.md)
- Sensor, lens family, aperture, focus, breathing, bokeh, shutter, motion blur, rolling shutter, highlight and flare behavior: [camera-optics-sensor.md](references/camera-optics-sensor.md)
- Reusable shot grammar distilled from notable filmmakers without direct style imitation: [director-shot-grammar-library.md](references/director-shot-grammar-library.md)

### Action and VFX

- Fight grammar, tactical beats, safety, ability choreography, and routing into hyperreal action-camera coupling: [action-direction.md](references/action-direction.md)
- CAVOK conditional fast-cut action signature and spatial safeguards: [cavok-action-signature.md](references/cavok-action-signature.md)
- Dedicated 2D hand-drawn anime combat grammar: key poses, silhouette, variable timing, smear, speed lines, impact frames, hand-drawn FX, background states, perspective exaggeration, character combat signatures, AI execution and QC: [2d-anime-combat-grammar.md](references/2d-anime-combat-grammar.md)
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
- Seedance 2.5 execution adapter: [seedance-2.5.md](references/seedance-2.5.md)
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

- Design blocking first. A camera move must clarify information, relationship, geography, emotional pressure, continuity, performer force, spatial transformation, or—in stylized 2D action—graphic force and pose readability.
- Choose movement from content rather than keywords. Sadness does not automatically mean push-in; danger does not automatically mean handheld; scale does not automatically mean drone; combat does not automatically mean sudden push-in, orbit, tracking, or shake.
- In live-action or grounded 3D, write active movement as: Start → Trigger / Motivation → Acceleration → Cruise / Follow / Yield → Deceleration → Settle → Hold → End.
- Let performers trigger the camera where appropriate; do not let the camera predict every reaction or release tension before the body does.
- In hyperreal combat, explicitly define the performer-camera timing relationship: character leads / camera follows, joint launch, camera yields, camera holds, or opposing vectors. Avoid automatic lockstep tracking.
- Stillness is an intentional camera behavior. Use Move → Settle → Discover → Hold → React → Move when continuous motion would dilute the beat. Action may begin with still camera + performance tell + character launch before camera response.
- In action, preserve attack vectors and geography, but do not equate clarity with permanent side-on full-body coverage. Use X/Y/Z staging, foreground, depth travel, elevation, diagonal vectors and near-lens passages.
- Unless intentionally stylized, do not stage two consecutive major attacks as pure lateral side views.
- Critical contact often benefits from camera deceleration or stability. Fast characters do not require maximum camera speed at impact.
- Camera shake is optional, not automatic. Use it only when force reaches the camera's physical or subjective position.
- Hyperreal action may use bold camera showmanship—weapon pass, body pass, ground skim, axial crash-in, vertical rise/dive, hidden cut, motivated axis crossing, reverse pull, vector match, shot-inside-shot—when each technique is visibly caused by character movement, force, environment, or information change.
- Use realistic support in live-action mode: Tripod, Dolly, Slider, Steadicam, Handheld, Gimbal, Crane/Jib, Drone, Vehicle Rig, Body Rig. Stylized CG virtual cameras may exceed physical rigs, but still require motivation, inertia and spatial logic.
- In 2D/anime mode, graphic camera and extreme perspective are allowed when they improve pose, vector, rhythm, or impact, but they must return to readable geography after abstraction.
- Avoid perpetual floating, automatic orbiting, random zooms, mechanically constant-speed moves, excessive 360-degree movement, meaningless shake, and camera travel through solid objects unless a clearly stylized animated rule makes the impossibility readable and purposeful.

## Hyperreal action non-negotiables

When directing live-action-feeling or hyperreal CG combat, load `hyperreal-action-direction-v2.md`.

- Camera does not decorate action; it inherits tension from performance, is triggered by action, and resolves with consequence.
- Design performer motion and camera motion as two coupled chains, not independent layers.
- Use three-dimensional staging: lateral, depth, vertical, and camera vector.
- Give each shot one dominant function: Geography, Performance, Threat, Mechanics, Immersion, Impact, Consequence, or Reorientation.
- Do not let every shot become a safe Mechanics Shot.
- Environment must affect performer or camera path through foreground occlusion, elevation, obstacles, reveals, damage, or spatial handoff.
- Reserve camera stunts for beats that benefit from them. A 10–15 second hero action passage should usually have about one true Hero Camera Move rather than constant maximum flair.
- Different fighters should have different camera-combat signatures.
- After contact, show at least one changed state: displacement, stance failure, weapon change, injury, environment damage, advantage reversal, distance change, elevation change, or emotional reassessment.
- If an AI model cannot execute a complex Hero Camera Move, split at a motivated occlusion or stable state rather than flattening the directing idea into generic lateral coverage.

## Optics non-negotiables

- Perspective follows camera position; focal length changes field of view, not physical perspective by itself, in photographic modes.
- Choose depth of field from information needs, not a blanket 'cinematic shallow focus' rule.
- Focus pulls need a motivated target, realistic speed, possible operator lag, and a stable landing.
- Shutter/motion blur must match the intended action language and every integrated VFX element.
- Flare, halation, chromatic effects, distortion and rolling-shutter stress require optical or sensor causes in photographic modes.
- Maintain lens/sensor behavior across shots intended to match.
- In hyperreal action, lens choice should participate in spatial choreography: ultra/wide lenses for near-far scale change and foreground passage, normal-wide for primary action geometry, longer lenses for compression, tactical pause or psychological pressure.
- In 2D/anime mode, explicit graphic perspective, smear, linework and background abstraction may replace photographic optics during designated beats; restore stable character proportions and spatial orientation afterward.

## VFX non-negotiables

In photographic modes, treat VFX as photographed abnormal physics, not game-skill decoration.

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

In 2D/anime mode, hand-drawn FX may become graphic rather than photoreal, but they must still obey source, vector, timing, contact, hierarchy, breakup and dissipation. FX cannot rescue an unreadable pose or erase the true contact point.

## Compositing non-negotiables

In live-action and hybrid modes:

- VFX must occupy a defined depth and obey foreground/background occlusion.
- Match plate focus, bokeh, shutter blur, lens distortion, atmospheric perspective, local exposure, grain and sharpness.
- Reflection/refraction must use the correct surface and background layer.
- Apply light wrap only when justified by bright neighboring light; never use a universal colored edge halo.
- Effects should not be sharper, cleaner or temporally more stable-looking than the photographed image around them.
- Audit temporal edge chatter, reflection flicker, matte boiling, distortion instability and grain swimming.

In pure 2D/anime mode, replace this audit with line continuity, color/paint continuity, smear restoration, FX-layer ordering, background-state continuity and stable key-pose identity.

## Atmosphere non-negotiables

In photographic modes, air is a spatial medium, not decoration. Fine dust or micro-particles remain sparse and become visible mainly in directional or back light. Volumetric haze must be thin enough to preserve faces, architecture, action and material detail. Atmospheric perspective should reduce distant contrast gradually. Avoid snow-like particles, full-screen floating light dots, thick fog, hard-edged god rays, and air effects that overpower the subject.

In 2D/anime mode, environmental media may be simplified into designed shapes or lines during action, but their direction must remain consistent with wind, pressure, and force, and they must not become random decorative noise.

## AI execution rules

- Keep directing intent model-independent until the target model and current capabilities are confirmed.
- Separate invariants from shot-specific state.
- Treat approved user decisions as locks. A local revision must not silently rewrite unrelated approved shots, blocking, dialogue, geography, wardrobe, VFX, or timing.
- Give every external reference an explicit responsibility: what to inherit, what not to inherit, and which approved version wins conflicts. Do not let a mood, color, pose, or motion reference silently override identity or geography.
- Use stable character aliases and approved reference assets.
- Prefer one major causal or graphic escalation per beat when model complexity is high.
- Enforce a practical Shot Complexity Budget: one narrative goal, one dominant character action, one primary camera idea, at most one secondary camera adjustment, one performance change, and one major FX/environment event unless the model and shot have been validated for more.
- In continuous time and space, next-shot start state must inherit previous-shot end state. Body posture, hands, support foot, momentum, restraint/contact, prop ownership, injury, elevation, and VFX state may change only through an observable event.
- Use short Continuity Risk Anchors only where a model is likely to reset state; do not duplicate the entire global bible at every shot.
- Write actions chronologically and observably; separate performer motion from camera motion, and explicitly connect them by trigger, lead/lag relationship, movement vector, contact behavior and settle. In 2D/anime mode also separate background-state changes and FX behavior.
- End multi-clip parts on stable readable states that can seed the next part.
- Use negatives only for likely or observed failures; excessive negatives compete with positive instructions.
- For hyperreal combat, design with `hyperreal-action-direction-v2.md` before model adaptation. Do not let an AI-model adapter silently flatten a three-dimensional or hero-camera design into generic side coverage; split at motivated transition points when needed.
- For 2D/anime combat, design with `2d-anime-combat-grammar.md` first. If the generation model is Seedance 2.5, translate the approved design through `seedance-2.5.md` afterward; the model adapter must not rewrite combat causality, key poses, character signatures, or geography.

## Failure handling

When diagnosing footage, preserve successful layers. Locate the earliest failure among story clarity, geography/POV, identity, blocking/pose, action-camera coupling, 3D staging, camera/focus/graphic perspective, action timing and spacing, material/VFX or hand-drawn FX, compositing/line integration, lighting/color, sound, temporal stability, or model limitation. Use the failure library before inventing a new fix. Correct one primary root cause at a time and define a success criterion for the next controlled test.

In hyperreal combat, specifically check for side-scroller syndrome, coverage syndrome, decorative camera syndrome, lockstep camera syndrome, over-showmanship, and impact blur syndrome before adding more camera movement.

## Regression discipline

After a major rule, routing or department-module change, run the cases in `tests/`. Score with `tests/scorecard.md`. No critical category may fall below 3/5; POV, causal-order and continuity violations are critical failures regardless of average. Do not accept a local improvement that materially regresses unrelated directing layers.

## Revision and execution discipline

- **Approved Lock:** preserve user-approved material outside the explicit revision scope.
- **Reference Responsibility Contract:** every image, video, keyframe, or asset reference has a bounded job and explicit non-responsibilities.
- **Physical State Ledger:** track body state, facing, gaze, left/right hands, support/weight, momentum, contact/restraint, injury, props and VFX state across shots.
- **Visible State Transition Law:** in continuous time/space, cuts do not perform state changes. If a character goes prone→standing, restrained→free, empty-handed→armed, airborne→grounded, or damaged→clean, the transition must be visible or an explicit time/location jump must establish the new state.
- **Continuity Risk Anchor:** repeat only the high-risk state likely to reset.
- **Sound Continuity State:** persistent beds and tails continue across contiguous shots, changing only with distance, occlusion, perspective, masking, damage, or an explicit source change.
- **Shot Complexity Budget:** if a beat exceeds the model's reliable execution budget, split at a stable state, motivated occlusion, or clear causal handoff rather than piling on more instructions.

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
3. Shot table with timecode, framing, camera, optics or graphic perspective, blocking/pose, image, sound, and continuity notes.
4. Character, environment, camera, optics/graphic rules, lighting/color, atmosphere, VFX/FX and compositing/line-integration locks as appropriate to the medium, plus explicit reference responsibilities when references are used.
5. For hyperreal combat, include performer-camera trigger/lead-lag logic and the sequence's key Hero Camera Move when relevant.
6. One chronological ready-to-use generation prompt or per-part prompts when duration requires splitting.
7. A targeted negative prompt.
8. Continuity, action readability, physical or graphic plausibility, action-camera coupling, spatial dimensionality, approved-lock preservation, reference-contract compliance, visible state transitions, sound continuity, integration and generation-feasibility checklist.

## Final principle

Control what the audience sees, knows, anticipates, and feels at each moment. The finished scene should behave like cinema or deliberate animation first; AI is only one production method.

For hyperreal action: **the performer creates the force, the camera interprets that force, the edit preserves its direction, and the consequence proves it happened.**