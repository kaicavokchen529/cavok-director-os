
# CAVOK Production, Previs & Evidence Gates

## Purpose

This module adds ten reusable decision systems for complex production, reference reconstruction, spatial previs, photographic plausibility, and controlled visual calibration.

It does not replace the CAVOK director chain. It runs before or alongside existing departments when uncertainty, reference dependence, spatial complexity, or long-form production makes premature shot design risky.

Core law:

> **Do not let an unverified assumption become production truth. Do not let an unverified space become camera blocking. Do not let an attractive effect become an unmotivated image rule.**

Use this module selectively. A simple self-contained shot should not inherit the overhead of a long-form production pipeline.

## Activation

Load this module when one or more conditions apply:

- long-form, multi-scene, or multi-episode work;
- complex interiors, multi-level spaces, pursuit routes, ensemble blocking, or action geography;
- important reverse angles or repeated coverage of the same location;
- reference-image / reference-video reconstruction;
- the user asks to reproduce, match, calibrate, or compare against a visual target;
- project facts contain uncertainty, inference, or director-added specificity;
- lighting, volumetrics, atmosphere, or depth carry major visual meaning;
- a generated result is close but wrong and needs controlled correction;
- repeated directing lessons are being promoted into reusable grammar.

For lightweight tasks, apply only the relevant gate instead of forcing the complete system.

# 1. Evidence State System

## Goal

Separate what the project knows from what the director infers or proposes.

Use five states:

~~~text
FACT
OBSERVATION
INFERENCE
DIRECTOR PROPOSAL
UNKNOWN
~~~

### FACT

Explicitly established by the user, approved script, project bible, confirmed continuity record, or other authoritative project source.

### OBSERVATION

Directly visible or audible in supplied evidence: image, frame, video, audio, diagram, or approved generated result.

Observation describes what the source actually supports, not the hidden production explanation.

### INFERENCE

A conclusion supported by available evidence but not directly established.

Examples include likely camera height inferred from perspective, probable room extension inferred from matching views, or possible light direction inferred from shadows.

### DIRECTOR PROPOSAL

A new production decision introduced because the scene requires specificity that the source does not provide.

Examples include an unseen corridor layout, a proposed practical light, or a camera route.

A proposal becomes a project lock only after approval when approval is required.

### UNKNOWN

Evidence is insufficient or contradictory.

Do not fill Unknown with decorative invention when the missing information affects geography, identity, continuity, camera, or causality.

## Promotion rule

Observation does not automatically become Fact.  
Inference does not automatically become Fact.  
Director Proposal does not automatically become Fact.

When a proposal is approved, record its new status in the project bible or relevant card.

Compact internal labels may be used when useful:

~~~text
F = Fact
O = Observation
I = Inference
D = Director Proposal
U = Unknown
~~~

# 2. Adaptive Production Readiness Gate

## Goal

Prevent premature shot design when unresolved upstream decisions would force later rework.

The gate is adaptive rather than mandatory for every scene.

## Readiness questions

Before detailed shot design, check:

1. Is the story / scene state sufficiently locked?
2. Are identity-critical characters and props defined?
3. Is the relevant space known well enough for the planned blocking?
4. Are entrances, exits, elevations, obstacles, destructible zones, and fixed light anchors known?
5. Are unresolved assumptions labeled as Inference, Proposal, or Unknown?
6. Will any unresolved item materially affect camera, action route, axis, VFX path, or continuity?
7. Is the target medium / reality mode established?
8. Are reference responsibilities explicit when references are used?

If an unresolved item materially affects execution, stop that affected layer and resolve or propose it first.

## Three readiness levels

### R0 — Lightweight

Use for a simple self-contained shot or short beat.

Needs dramatic purpose, subject state, basic geography, camera intent, and continuity entry / exit.

### R1 — Scene Production

Use for repeated coverage, dialogue geography, moderate action, or continuity-sensitive AI generation.

Add scene card, physical state ledger, reference contract, key environment anchors, approved locks, and start / end state.

### R2 — Spatial Previs

Use for complex action, ensemble movement, multi-level geometry, long continuous blocking, or repeated reverse angles.

Require a spatial representation before final camera choreography.

Core rule:

> **Production readiness is determined by dependency risk, not by prestige or duration.**

A 12-second fight may require R2. A two-minute monologue in one locked position may remain R1.

# 3. Spatial Previs + Blocking Map

## Goal

Build world space before screen space when geography materially affects directing.

## Previs sequence

~~~text
Evidence / Environment References
→ Common Spatial Anchors
→ World-Space Reconstruction
→ Neutral Spatial Base
→ Character Blocking Overlay
→ Camera / Axis Overlay
→ Feasibility Check
→ Shot Design
~~~

### Common anchors

Use persistent features such as walls, corners, doors, windows, stairs, ledges, railings, fixed furniture, columns, road edges, fixed practical lights, and environmental landmarks.

### One world

Different views must represent the same world coordinates.

A reverse angle is not a horizontal mirror of the forward angle.

If evidence conflicts, mark the conflict. Do not force incompatible references into one room.

### Neutral spatial base

Before camera choreography, maintain a neutral plan / node map containing orientation, approximate scale, anchors, entrances / exits, usable floor, elevation, and unknown regions.

Proposed camera blocking may not silently alter this geometry.

### Blocking overlay

Add character start / end positions, facing, gaze, movement paths, action zones, interaction points, obstacles, and contact areas.

### Camera overlay

Only after blocking is plausible, add camera positions, view vectors, camera paths, primary axis, motivated axis crossings, readable side when relevant, and expected visible background.

## Feasibility questions

- Can the performer physically travel the route?
- Does the camera actually see the claimed background?
- Does the move pass through walls, props, bodies, or impossible geometry?
- Are reverse angles derived from the same world?
- Does lens / distance fit the available space?
- Can the camera stunt be supported by performer movement?
- Does a Hero Camera Move require depth or environment the set does not provide?

Spatial previs constrains geography, not creativity. Once geography is stable, performance, action, and camera may become highly expressive inside it.

# 4. Light Source Causality

## Goal

Treat lighting as a causal system, not an emotional adjective.

Every narratively important photographic light should answer:

~~~text
Source
→ Scene Anchor
→ Direction
→ Landing
→ Falloff / Occlusion
~~~

### Source

What produces the light: sun, sky, window, fixture, fire, screen, vehicle light, VFX source.

### Scene Anchor

Where is the source in the world? The anchor remains spatially consistent across coverage unless the source moves.

### Direction

What path does the light take relative to subject and camera?

### Landing

Which face plane, body area, prop, floor, wall, atmosphere, or environment receives it?

### Falloff / Occlusion

Why does another region become darker, softer, blocked, reflected, or colored?

Invisible support light is allowed only when it behaves like plausible bounce or extension of an existing lighting system. It must not create a new unexplained key, rim, or eye light.

Emotion may influence blocking, exposure, timing, or practical events. Emotion alone does not teleport a light source.

# 5. Single Dominant Depth Mechanism

## Goal

Avoid cinematic depth created by stacking fog, shallow focus, foreground clutter, rim light, and blur without a clear spatial cause.

For a shot whose depth is visually important, choose one dominant mechanism.

## A — Light / Exposure Separation

Use when foreground, subject, and background occupy meaningfully different motivated light zones.

## B — Atmospheric Perspective

Use for genuinely long distances where air, humidity, dust, sea atmosphere, smoke, or natural scattering reduces distant contrast.

Primary behavior:

- contrast decreases with distance;
- saturation may reduce gradually;
- distant color shifts toward environmental scattering;
- structures remain spatially legible.

Atmospheric perspective is not generic blur.

## C — Occlusion / Scale Recession

Use existing geometry, repeated structures, bodies, terrain, vehicles, architecture, or object scale.

Primary behavior:

- functional foreground overlap;
- middle-ground subject;
- structures reduce / overlap with distance;
- route or vanishing direction remains readable.

Other cues may exist, but remain subordinate.

> **Depth must have a dominant cause.**

When prompt budget becomes crowded, preserve identity, action, contact, and causality before decorative depth language.

# 6. Volumetric Double Gate

## Goal

Prevent unsupported fog, god rays, glowing dust, and generic volumetric atmosphere.

Visible volumetric light requires both:

~~~text
REAL MEDIUM
+
NAMED DIRECTIONAL LIGHT SOURCE
~~~

## Gate A — Medium

Identify the medium and why it exists: smoke, dust, steam, mist, rain aerosol, snow, sea spray, water suspension, local gas, exhaust, or debris plume.

Specify where it is and how dense / local it is.

## Gate B — Light

Identify the source: window, doorway, sun, searchlight, headlight, fire, practical fixture, or VFX emission.

Specify direction, obstruction, landing, and falloff.

## If both pass

The medium may reveal the light only in the relevant path. Outside that path, air should remain comparatively clean.

The effect must not erase face, attack path, silhouette, exit route, or background structure needed for geography.

## If either fails

Remove visible volumetric language and use another depth mechanism.

## Special environments

- Vacuum: no atmospheric fog or air beams; local exhaust / gas / debris remains local.
- Underwater: use water suspension, bubbles, sediment, or disturbed particulate, not air fog.
- Clean interior: default to clean air unless the story creates a medium.

# 7. Director Mechanism Module + Anti-Trigger

## Goal

Store directing knowledge as decision mechanisms, not style labels or surface motifs.

A reusable mechanism module should follow:

~~~text
Activation Conditions
→ Dramatic Problem
→ Decision Mechanism
→ Blocking / Camera / Editing Consequence
→ Visible Result
→ Exit Condition
→ Anti-Trigger
→ Evidence / Validation Notes
~~~

### Activation Conditions

What dramatic or spatial problem makes the mechanism useful?

### Dramatic Problem

What must the audience understand, anticipate, feel, or re-evaluate?

### Decision Mechanism

What causal directing logic solves it?

Examples include reaction-before-reveal, action causality, procedural control, delayed scale perception, or spatial permission.

### Consequence

Translate the mechanism into blocking, gaze, camera position, camera timing, shot function, editing, sound, light, and spatial reorientation.

### Visible Result

Describe what should actually be evident on screen.

### Exit Condition

State when the sequence should leave this mechanism or return to another grammar.

### Anti-Trigger

List surface traits insufficient to activate it.

Examples:

- symmetry alone is not a reason to invoke graphic-tableau grammar;
- smoke and backlight alone do not activate world-geometry atmosphere grammar;
- fast cutting alone does not activate kinetic causality;
- a push-in alone does not equal tension;
- a long take alone does not imply observational duration grammar.

CAVOK should prefer transferable causal knowledge over imitation of named artists.

# 8. Geometry Before Lens

## Goal

Fix spatial projection before treating focal length as the primary solution.

For reference reconstruction or shot matching, use this order:

~~~text
Frame / Crop
→ Subject Position & Occupancy
→ Camera / Subject / Background Relative Distance
→ Horizon / Perspective / Occlusion
→ Field of View / Lens Candidate
→ Depth of Field
→ Optical Texture
~~~

Perspective is primarily controlled by camera position relative to the world.

Changing focal length without fixing camera / subject / background relationship often preserves the spatial error.

Record first:

- effective aspect / crop;
- subject height in frame;
- eye line;
- horizon;
- major object positions;
- foreground overlap;
- camera height;
- subject distance;
- subject-to-background distance.

When absolute measurements are unknown, use relative relationships and candidate solutions.

Treat focal length as a human communication aid and a candidate consistent with required field of view, not a magically unique answer derived from one still.

For AI execution, visible results often matter more than metadata: natural vs exaggerated perspective, background compression, near-far scale change, subject occupancy, and depth readability.

# 9. Evidence Boundary

## Goal

Never claim that a source proves more than it can.

## A static image can support

- composition;
- screen position;
- pose at that instant;
- visible material;
- lighting appearance;
- depth cues;
- blur visible in that frame;
- approximate perspective;
- visible environment state.

## A static image cannot independently prove

- camera path;
- camera speed;
- shot duration;
- cut timing;
- complete action direction;
- complete performance arc;
- before / after staging;
- production equipment;
- hidden light placement.

## Video can support

Only what is actually visible / audible in the inspected interval: temporal action, camera movement, edit points, sound timing, reaction order, and continuity changes.

Do not generalize one clip into an entire production style without broader evidence.

Use explicit language:

- **Observed:** source directly shows this.
- **Inferred:** evidence suggests this.
- **Designed:** this is CAVOK's new solution.
- **Unverified:** source does not establish this.

If no generated output has been viewed, say the directing plan / prompt structure has been checked; visual execution is not yet verified.

Text compliance is not visual validation.

# 10. Matched Dimension Lock + Calibration Loop

## Goal

Correct the biggest visible error without destroying dimensions that already work.

## Comparison order

When comparing a generated result against the target or approved design, inspect:

~~~text
Approved Locks
→ Crop / Frame
→ Identity / Key Props
→ Blocking / Pose
→ Geometry / Perspective
→ Camera Motion / Timing
→ Light / Exposure
→ Color
→ Material / Optical Texture
→ VFX / Atmosphere
→ Sound / Edit
~~~

Reorder only when project priorities demand it.

For each important dimension, record:

~~~text
MATCHED
DEVIATION
NOT EVALUABLE
~~~

Do not hide mismatch by cropping away the error.

## Matched Dimension Lock

Before a retry, record:

~~~text
Already Correct:
Current Primary Failure:
Likely Cause:
Change This:
Protect:
Success Criterion:
~~~

Example:

~~~text
Already Correct:
identity, weapon path, contact timing

Current Primary Failure:
camera feels too lateral

Likely Cause:
insufficient Y-axis performer travel and camera remains outside action corridor

Change This:
performer depth route + camera participation

Protect:
identity, attack order, weapon contact, lighting direction

Success Criterion:
same tactical exchange reads with clear near/far displacement and no side-scroller flattening
~~~

## Calibration loop

~~~text
Observe
→ Classify
→ Select Largest Error
→ Hypothesize Cause
→ Change One Cause Group
→ Protect Matched Dimensions
→ Regenerate / Re-evaluate
→ Check Improvement & Regression
~~~

If repeated targeted corrections do not improve the result, change the control method, reduce complexity, split the generation, or report a model / tool boundary.

Do not repeatedly submit the same overloaded prompt and call that progress.

# How the Ten Systems Work Together

For a complex production:

~~~text
Evidence State
→ Production Readiness
→ Spatial Previs
→ Performance / Blocking
→ Camera / Action Choreography
→ Light Causality
→ Dominant Depth Mechanism
→ Volumetric Gate
→ AI Execution
→ Evidence-Bounded Review
→ Matched-Dimension Calibration
~~~

Director Mechanism Modules can influence performance, blocking, camera, editing, sound, and reveal strategy throughout this chain, but may not override project facts, locked geography, physical lighting logic, or continuity.

# Interaction with Existing CAVOK Modules

- **director-framework.md** owns story intent, POV, dramatic beats, and the general director chain. This module adds readiness and evidence gates before high-risk execution.
- **continuity-direction.md** owns state transitions. Spatial Previs supplies stable world coordinates for continuity to track.
- **art-assets.md** owns Reference Responsibility Contracts. Evidence State clarifies whether a reference property is observed, inferred, or newly designed.
- **camera-shot-decision-system.md** owns final shot decisions. Geometry and Spatial Previs should be resolved first when space is uncertain.
- **camera-optics-sensor.md** owns optics. Do not use optics to compensate for unresolved geometry.
- **cinematic-lighting.md / lighting-atmosphere.md** own photographic execution. Light Source Causality, Dominant Depth, and Volumetric Double Gate constrain them upstream.
- **director-shot-grammar-library.md** should store future reusable directing experience in the mechanism + Anti-Trigger format.
- **generation-diagnostics.md** owns failure diagnosis. Matched Dimension Lock prevents local corrections from regressing successful layers.
- **ai-video-execution.md** owns model translation. It receives resolved facts, geometry, locks, and execution-critical causality, not the entire internal reasoning archive.

# What This Module Does Not Adopt as Universal Law

The following may be useful project strategies but are not global CAVOK rules:

- absolute five-second maximum shot duration;
- mandatory twenty-second grouping;
- mandatory shot-size change at every cut;
- mandatory forward / reverse reference pair for every location;
- mandatory HEX percentages in every generated shot;
- mandatory numeric lighting ratio in every prompt;
- mandatory full spatial-previs approval for simple scenes.

Use these only when the production or target model benefits from them.

# Compact QC

Before a complex scene leaves preproduction:

1. Are Fact, Observation, Inference, Proposal, and Unknown separated?
2. Is the scene at the correct readiness level?
3. If geography is complex, does one world-space map exist before camera design?
4. Are reverse views derived from the same world rather than mirrored?
5. Can every important light identify source, anchor, direction, landing, and falloff?
6. Does each depth-heavy shot have one dominant depth mechanism?
7. Does visible volumetric light pass both medium and directional-source gates?
8. Are reusable director rules stored as mechanisms with Anti-Triggers rather than surface style labels?
9. Was geometry solved before lens attribution?
10. Are claims bounded by actual evidence?
11. Before a retry, are already-correct dimensions explicitly protected?
12. Is visual validation claimed only after actual output has been inspected?

## Final principle

> **Verify the world before photographing it, verify the evidence before naming it truth, and protect what already works before changing what does not.**
