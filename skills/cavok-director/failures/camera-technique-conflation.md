# Failure: Camera Technique Conflation

## Symptom

The plan names an impressive technique, but the observable shot behavior is ambiguous or contradictory. “急推” becomes an unspecified zoom, “后拉” does not say whether camera position changes, “俯拍” is treated as a downward move, or “子弹时间” is written as generic slow motion.

## Diagnosis

The design collapsed four separate systems:

- camera position and physical travel;
- lens and optical change;
- angle/elevation state;
- temporal behavior.

Because the mechanism is unresolved, AI execution chooses an arbitrary interpretation and continuity cannot be checked.

## Fix

Resolve the shorthand before prompt delivery:

1. State whether the camera physically moves and how parallax changes.
2. State whether focal length or focus changes while position remains fixed.
3. State the camera height, downward/upward pitch, and whether those values change.
4. State subject, world, camera, and audio time rates plus entry and exit triggers.
5. Give the move a start composition, trigger, speed curve, landing, hold, and exit.

## Preventive rule

Never accept a technique label as execution. Translate it into observable mechanics and reject incompatible combinations before generating the shot plan.
