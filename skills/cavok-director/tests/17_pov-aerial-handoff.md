# Test 17 — POV and Aerial Handoff

## Brief

Design a continuous-feeling action passage that begins with a high aerial view of a rooftop route, descends into an FPV-drone pursuit through structural gaps, hands off to a grounded Steadicam follow, briefly enters embodied first person during an impact, and returns to an objective consequence shot.

## Requirements

- State what new information each viewpoint regime provides.
- Give the drone and FPV camera flyable routes, altitude changes, obstacle order, target reacquisition, and arrival states.
- Make the FPV-to-Steadicam and third-person-to-first-person transitions visible or editorially motivated.
- Preserve target identity, screen direction, speed, spatial anchors, and action state across handoffs.
- Treat first person as a body with gaze, balance, contact, and limited information.
- Translate platform labels into observable camera behavior.
- Split the generation at motivated occlusion or stable state if one continuous shot exceeds model capability.

## Critical failures

- “Drone shot,” “FPV,” “Steadicam,” or “first person” appears only as a label.
- Camera passes through solid structure without an approved virtual-camera rule.
- Handoff reverses route or momentum without cause.
- First person behaves like a floating external camera.
- Aerial scale does not reveal any spatial fact.
- The model adapter removes the approved viewpoint arc instead of segmenting it.
