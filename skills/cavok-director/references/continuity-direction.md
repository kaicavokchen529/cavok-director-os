# Continuity Direction

## Purpose

Protect the scene state across shots, generations, revisions, and tools. Treat continuity as a state transition system rather than a final visual check.

## Build the continuity bible

Lock:

- character identity, proportions, face, hair, wardrobe layers, accessories, footwear, and distinguishing marks;
- prop identity, owner, hand, orientation, condition, and location;
- geography, screen direction, elevation, eyelines, entrances, exits, and distances;
- weather, time, light direction, exposure, surface wetness, atmosphere, and wind;
- emotional knowledge, relationship distance, breath, fatigue, injury, dirt, blood, and ability cost;
- physical body state: standing, sitting, kneeling, prone, airborne, restrained, carried, braced, leaning, falling, or recovering;
- head/gaze direction, left-hand state, right-hand state, support foot / weight distribution, momentum, contact relationship, and load-bearing relationship;
- destruction, debris, frost, scorch, smoke, water, and other VFX residue.

Separate **invariants** from **shot state**. Invariants cannot drift without a story reason. Shot state changes only through an observable event.

## Physical State Ledger

For continuity-critical characters, track:

```text
World position:
Body state:
Facing:
Head / gaze:
Left hand:
Right hand:
Weapon / prop:
Support foot / weight:
Momentum:
Contact / restraint / load relationship:
Injury / blood / dirt:
Costume damage:
Breath / fatigue:
Emotional knowledge:
```

Do not reduce continuity to screen-left / screen-right. Screen position is a projection of the current camera; world position is the persistent spatial state.

## Track state transitions

For every shot, record incoming state, scripted change, and outgoing state. Use frame references for contact, separation, prop exchange, injury, destruction, and ability activation.

```text
Shot:
Incoming state:
Trigger:
State change:
Outgoing state:
Next-shot obligations:
```

Preserve action match: gaze, hand position, support foot, momentum, breath phase, fabric direction, debris motion, and focus distance. If two characters begin in contact, define the exact trigger and mechanics of separation.

## Visible State Transition Law

In continuous time and space:

> **Next-shot start state = previous-shot end state.**

Any difference between those states must be caused by a visible event in one of the shots. A cut does not grant permission to change body state, prop ownership, restraint, injury, weapon hand, elevation, or momentum.

Legal transitions:

1. complete the transition before the cut;
2. begin the next shot from the inherited state and show the transition;
3. insert a dedicated transition shot;
4. use an explicit time / location jump and establish the new state.

Illegal examples include prone → standing, kneeling → walking, restrained → free, empty hand → armed, airborne → grounded, or damaged → clean without an observable cause.

At high-risk transitions, use a compact **Continuity Risk Anchor** rather than repeating the full bible, for example:

```text
Continuity anchor: she begins this shot still on one knee; only the camera position changes.
```

Use risk anchors only where the model is likely to reset or reinterpret state.

## Generate across multiple clips

End each clip on a stable, readable state that can seed the next clip. When possible, choose an end state with clear body support, readable hands / props, stable geography, and low ambiguity. Provide the next generation with:

- approved final frame or reference images;
- compact invariant block;
- outgoing pose and gaze;
- environmental and VFX residue;
- explicit forbidden resets.

Do not repeat the entire scene description if it increases conflict. Repeat only identity anchors and continuity obligations.

## Audit

Check in this order: identity, geography, action, props, damage, lighting, environment, VFX residue, sound perspective. Mark discrepancies as intentional, acceptable, repairable in post, or requiring regeneration.

