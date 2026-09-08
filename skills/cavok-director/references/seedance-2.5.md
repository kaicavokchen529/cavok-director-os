# Seedance 2.5 Execution Adapter

## Status and scope

Target: ByteDance Seedance 2.5.

Last capability check: 2026-09-08.

This module translates CAVOK directing intent into Seedance 2.5 generation, reference-generation, extension, and editing prompts. Keep story, blocking, camera, action, lighting, VFX, and continuity decisions model-independent first; use this adapter only at the execution layer.

Officially documented capabilities relevant to directing include:

- up to 30 seconds in one generation;
- multi-round video extension;
- timestamp-scoped control of narrative, camera perspective, movement, and pacing;
- multimodal reference with up to 30 images, 10 video clips, and 10 audio clips in one pass;
- explicit reference use for characters, scenes, props, composition, motion, camera language, lighting, and style;
- clay-render / white-model reference for camera movement, shot-size transitions, subject trajectory, blocking, and spatial structure;
- targeted editing that can preserve unaffected content while changing characters, actions, plot, camera perspective, or other requested elements;
- improved long-form multi-shot continuity, while complex motion and multi-subject interaction can still fail physically or spatially.

Capability limits and UI behavior may change. Re-check the official Seedance 2.5 interface or documentation before relying on exact input counts, duration, extension count, or edit controls in production.

## Activation rules

Load this adapter when the target model is explicitly Seedance 2.5.

Inside the CAVOK project, `SD2.5` may be treated as shorthand for Seedance 2.5 when the surrounding task is AI video generation. Outside that context, confirm the model name if `SD2.5` is ambiguous.

When this adapter is active, do not rewrite the directing concept merely to imitate a generic Seedance example. Preserve CAVOK causality, geography, body mechanics, camera motivation, optical behavior, and continuity; only change the execution structure and model-facing wording.

## Core mental model

Seedance 2.5 prompts should be treated as a **directed temporal program with reference contracts**, not as a bag of style keywords.

Use this hierarchy:

```text
TASK / MODE
→ REFERENCE CONTRACT
→ GLOBAL INVARIANTS
→ CONTIGUOUS TIMELINE
→ END STATE / CONTINUITY HANDOFF
→ TARGETED KEEP / NEGATIVE CONSTRAINTS
```

The model should know, in this order:

1. what kind of operation it is performing;
2. what each reference is responsible for;
3. what must remain stable across the whole clip;
4. what changes over time and in what causal order;
5. what state the clip must end on;
6. what high-risk failures must be prevented.

## 1. Task / mode first

State the operation before scene prose.

Typical modes:

- Generate: create a new clip from text and/or references.
- Reference-to-video: create a new clip while assigning explicit responsibilities to images, videos, audio, or clay renders.
- Extend: continue from an existing video and inherit its outgoing state.
- Edit: modify only a requested layer or time range while preserving the rest.

Do not mix generation, extension, and edit language unless the actual interface/task requires it.

## 2. Reference Contract

Seedance 2.5 can understand many reference materials, but more references do not automatically mean more control. Every important reference should have a declared job.

Write references by **authority and function**:

```text
@Image 1: strict character identity — face, hair, body proportion, costume only.
@Image 2: environment architecture, scale, materials, and daylight condition only.
@Video 1: action timing and body mechanics only; do not inherit character identity or background.
@Clay Render 1: camera path, shot-size transitions, blocking, spatial relationships, and motion trajectory.
@Audio 1: voice / sound texture only, if audio generation is required.
```

### Reference rules

- Separate identity reference from pose/action reference whenever possible.
- Separate environment/layout reference from mood/style reference when they could conflict.
- For a character identity anchor, use strong language such as `strictly follow` only for the attributes that truly must not drift.
- If two references could conflict, explicitly define which one owns identity, blocking, camera, material, lighting, or style.
- Do not let a mood image silently override geography or character identity.
- Do not say only `reference all images`; assign responsibilities.
- Clay render is the preferred control source when exact blocking, trajectory, camera position, or shot transition is more important than surface appearance.

## 3. Global Invariants

After the references, define only the facts that must remain stable throughout the clip.

Useful global locks:

- aspect ratio, reality level, overall image mode;
- stable character aliases and identity anchors;
- wardrobe and prop state;
- environment layout and major landmarks;
- time of day, weather, key-light direction, wind direction;
- camera family / optical behavior when continuity requires it;
- overall color and material rules;
- sound policy if relevant;
- forbidden global resets.

Do not repeat the full character and environment description inside every timestamp block. Stable information belongs here; changing information belongs in the timeline.

## 4. Contiguous Timeline

Seedance 2.5 officially supports timestamp-scoped prompting. Use time ranges as **beat boundaries and pacing control**, not as a promise of frame-perfect choreography.

Write time continuously:

```text
0–4s
4–8s
8–13s
13–18s
18–24s
24–30s
```

Avoid unexplained time gaps and excessive 0.05–0.1 second micro-segmentation unless editing a specific existing clip requires it.

### Beat contract

Within each time range, order information as:

```text
Shot size / angle
→ Camera behavior
→ Initial composition / blocking
→ Subject action in chronological order
→ Contact / state change / result
→ Environment / VFX response
→ Sound cue if required
```

Example skeleton:

```text
8–12s: lateral medium-wide. Dolly/track begins only after the performer launches, follows slightly late, then decelerates and settles. Character A pivots from the support foot, crosses the gap, makes contact with B, and B is displaced toward the rear-left obstacle. Dust and cloth react after the body impulse. End with A grounded and B at the new position.
```

### Timeline rules

- One dominant causal change per beat when action or VFX complexity is high.
- Protect preparation, contact, consequence, and recovery.
- After teleportation, knockback, large vertical movement, scene change, or major destruction, include a readable spatial re-anchor.
- If a cut occurs, describe the new shot and its purpose; do not assume the model will infer a clean edit from prose alone.
- If the shot remains continuous, explicitly say `single continuous take / no cut` only when that continuity is important.
- Do not force every beat to occupy equal duration. Duration follows information density and action readability.
- 30 seconds is a capacity, not a target. Use only the duration the scene needs.

## 5. Separate camera motion from subject motion

Do not compress performer motion and camera motion into one ambiguous sentence.

Preferred order:

```text
Camera: support + position + movement + trigger + speed curve + settle.
Subject: position + facing + action + contact + recovery.
```

For active movement, keep CAVOK's motion curve:

```text
Start → Trigger → Acceleration → Travel → Deceleration → Settle → Hold
```

Seedance 2.5 supports sophisticated camera instructions, but stacking several competing moves still increases failure risk. Prefer one primary camera change per beat.

## 6. Long-form 30-second storytelling

Seedance 2.5 is better at organizing multiple connected shots within 30 seconds, but CAVOK should not equate longer duration with more spectacle.

Build 30-second clips around **state progression**:

```text
entry state
→ immediate dramatic problem
→ escalation / change
→ consequence or reversal
→ exit state
```

A sequence may continue unresolved if the story requires it. The final beat should still end in a clear state that can seed the next generation.

For complex combat, multi-character interaction, or dense VFX, reduce simultaneous changes before adding more prose. The official release notes still identify complex physical motion and multi-subject interaction as areas with remaining room for improvement.

## 7. Transitions and multi-shot continuity

Seedance 2.5 can perform multiple shots and smoother transitions, but transitions should still have a visible or auditory handoff.

Useful transition anchors:

- action match;
- eyeline / attention shift;
- foreground occlusion;
- object pass close to lens;
- pan/tilt landing on new information;
- sound bridge;
- stable result frame followed by a motivated cut.

Do not ask for a transition only because it sounds cinematic. The transition must preserve geography, identity, state, or narrative flow.

## 8. Extension prompts

When extending a generated clip, inherit the outgoing state before introducing new events.

Use:

```text
Continue from @Video 1.
Keep the main subjects, environment, visual style, camera/optical behavior, damage state, atmosphere, and sound perspective consistent.
Start exactly from the outgoing positions, facing directions, body momentum, props, destruction, and VFX residue of @Video 1.
Then continue with: ...
```

Do not reset character pose, damage, environment, light direction, or VFX state at the start of an extension unless a visible event causes the change.

## 9. Editing prompts

For editing, use the narrowest possible scope.

Preferred structure:

```text
Edit @Video 1.
Keep [protected layers] unchanged.
Change only [target layer].
Time range: X–Ys.
Before Xs and after Ys, preserve the original continuity unless the edit necessarily changes the physical result.
```

Examples of protected layers:

- character identity;
- action timing;
- environment;
- lighting;
- camera;
- audio;
- color / material;
- background extras.

Do not regenerate the entire scene description when only camera, one action beat, one prop, or one time range is wrong.

## 10. Audio

Seedance 2.5 is an audio-video joint generation model. If generated sound is required, place audio instructions at the beat where the physical cause occurs and preserve distance/material perspective.

If music will be added in post, say so briefly only when the active interface tends to generate unwanted music; otherwise do not waste prompt budget on BGM prose.

When using audio references, state whether they own voice identity, ambience, Foley texture, rhythm, or another specific property.

## 11. Action and VFX execution

Seedance 2.5's stronger long-form and reference control does not remove the need for physical choreography.

For action, preserve:

```text
intention
→ preparation / support
→ attack vector
→ contact
→ compression / force transfer
→ consequence
→ recovery
→ new state
```

For VFX, preserve:

```text
precursor
→ formation
→ material / optical behavior
→ contact
→ environmental response
→ residual / dissipation
```

Do not use prompt length to compensate for missing physical logic. If the model cannot execute a complex beat reliably, split at a stable state or use clay-render/action references.

## 12. Prompt density and priority

Seedance 2.5 can understand longer narrative prompts, but attention is still finite.

Priority inside an execution prompt:

1. reference responsibilities;
2. identity and geography invariants;
3. chronological subject action;
4. camera behavior;
5. contact / state change;
6. lighting and atmosphere;
7. VFX / material detail;
8. sound;
9. targeted negatives.

Delete decorative synonyms that do not change an observable result.

## 13. Negative constraints

Use negatives as a short failure-control layer, not as a second prompt.

Good negatives are specific to likely errors:

```text
no identity drift;
no screen-direction swap;
no camera orbit;
no pose reset after the cut;
no generic explosion replacing contact;
no global color spill from a local VFX source.
```

Avoid long walls of synonymous negatives. Positive chronological instructions should carry most of the control.

## 14. Seedance 2.5 prompt template

```text
[TASK]
Generate / Reference-to-video / Extend / Edit.
Duration / aspect ratio / continuity mode.

[REFERENCE CONTRACT]
@Image / @Video / @Clay Render / @Audio: exact responsibility of each reference.

[GLOBAL INVARIANTS]
Character identity; wardrobe; props; environment geography; time/weather; light/wind direction; camera/optical family; visual/material rules.

[0–Xs]
Shot size and angle. Camera start/trigger/move/settle. Initial blocking. Subject action in chronological order. State change. Environment/VFX/sound response.

[X–Ys]
Next beat with inherited incoming state and one dominant new change.

[Y–END]
Payoff / consequence / transition. End on a readable outgoing state.

[END STATE]
Exact final positions, facing, pose, damage/props, environment destruction, VFX residue, camera state, and transition obligation.

[KEEP / NEGATIVE]
Only high-risk preservation and failure constraints.
```

## 15. What not to do

Avoid:

- keyword soup with no causal timeline;
- assigning no role to reference assets;
- asking one reference to control identity, pose, scene, camera, and lighting when those properties conflict;
- repeating the entire character bible in every beat;
- frame-micromanaging a 30-second generation with dozens of tiny timestamp windows;
- several competing camera moves in one beat;
- camera and performer movement written as one ambiguous motion;
- 30 seconds of constant escalation with no spatial/result anchors;
- using more adjectives when the real problem is blocking or chronology;
- rewriting unaffected layers during a targeted edit;
- treating negative prompts as the main control mechanism.

## Final principle

For Seedance 2.5, prompt quality is primarily **reference assignment + temporal causality + stable state management**.

The strongest prompt is not the longest prompt. It is the one that makes clear:

> what each reference controls, what is invariant, what changes now, what the camera does in response, what physical result follows, and what state must survive into the next beat.
