# Deliverable Templates

## Contents

1. Scene brief
2. Shot table
3. Generation prompt
4. VFX design block
5. Continuity audit
6. Evolution log

## 1. Scene brief

```text
Format / duration:
Genre and reality level:
Scene objective:
Conflict or obstacle:
Entry state:
Exit state:
Audience information:
Viewpoint owner by beat:
Location geography:
Character invariants:
Continuity-critical actions and props:
```

## 2. Shot table

| Shot | Time | Viewpoint | Size / angle | Camera behavior | Blocking and performance | Image / lighting / VFX | Sound | Continuity purpose |
|---|---:|---|---|---|---|---|---|---|
| 01 | 00:00–00:03 |  |  |  |  |  |  |  |

Keep each row centered on one beat. If a shot contains several actions, state their exact order.

## 3. Generation prompt

```text
[FORMAT LOCK]
Duration, aspect ratio, frame rate, live-action/animation reality level, no subtitles if required.

[INVARIANTS]
Stable character identities, wardrobe, props, geography, weather, time of day, light direction.

[00:00–00:XX]
Viewpoint owner; framing; initial composition; character action and gaze order; camera start, movement, arrival, and hold; sound.

[00:XX–00:YY]
Trigger; reaction order; blocking transition; focus or viewpoint change; lighting and environmental response.

[00:YY–END]
Payoff; contact and consequence; aftermath; final composition and clean transition point.

[QUALITY LOCK]
Observable realism rules appropriate to camera, acting, action, materials, lighting, sound, and VFX.

[NEGATIVE CONSTRAINTS]
Only likely or previously observed failures.
```

## 4. VFX design block

```text
Source:
Precursor:
Formation:
Material:
Propagation:
Lighting interaction:
Contact behavior:
Secondary physics:
Performer response:
Sound:
Aftermath and dissipation:
```

## 5. Continuity audit

```text
[ ] Viewpoint ownership is explicit and causally correct.
[ ] Screen direction and geography remain readable.
[ ] Character identity, wardrobe, props, and injuries remain stable.
[ ] Contact and separation occur only at scripted triggers.
[ ] Hands, gaze, weight, and momentum connect across cuts.
[ ] Camera moves have motivated starts and stable arrivals.
[ ] Light direction and exposure remain consistent.
[ ] VFX source, path, material, interaction, and lifecycle are complete.
[ ] Sound matches distance, material, and timing.
[ ] Final frame creates a usable edit point.
```

## 6. Evolution log

```text
Project:
Scene:
Model / version:

What worked:
-

What failed:
-

Model-specific error:
-

Reusable rule learned:
-

Next controlled test:
-
```

