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
- destruction, debris, frost, scorch, smoke, water, and other VFX residue.

Separate **invariants** from **shot state**. Invariants cannot drift without a story reason. Shot state changes only through an observable event.

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

## Generate across multiple clips

End each clip on a stable, readable state that can seed the next clip. Provide the next generation with:

- approved final frame or reference images;
- compact invariant block;
- outgoing pose and gaze;
- environmental and VFX residue;
- explicit forbidden resets.

Do not repeat the entire scene description if it increases conflict. Repeat only identity anchors and continuity obligations.

## Audit

Check in this order: identity, geography, action, props, damage, lighting, environment, VFX residue, sound perspective. Mark discrepancies as intentional, acceptable, repairable in post, or requiring regeneration.

