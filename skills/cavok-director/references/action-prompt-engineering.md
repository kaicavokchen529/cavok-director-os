# Action Prompt Engineering

## Contents

1. Separate direction from execution prompts
2. Build a causal action chain
3. Allocate time and shot density
4. Express speed and force visibly
5. Motivate action camera movement
6. Protect identity and body proportions
7. Handle rotations, chases, and environmental impacts
8. Write the compact model prompt
9. Diagnose common failures
10. Audit

## 1. Separate direction from execution prompts

Maintain two layers:

- **Director layer:** intention, tactics, geography, coverage, continuity, editorial options, and internal style vocabulary.
- **Model layer:** chronological visible events, exact subjects, one primary camera behavior, contact, consequence, and only failure-specific negatives.

Do not send an unexplained internal label such as a CAVOK action-mode name to a video model and expect reliable behavior. Translate it into observable instructions such as: short preparation, explosive release, hard deceleration at contact, immediate displacement, and no neutral reset.

Remove explanations written for collaborators from the model prompt. Avoid repeating the same rule in the style block, every shot, and the negative prompt.

## 2. Build a causal action chain

Design every exchange in this order:

```text
incoming state
→ visible trigger
→ preparation tell
→ attack line
→ defense or evasion
→ contact or near miss
→ momentum transfer
→ consequence
→ outgoing state that prepares the next move
```

Make the previous result become the next preparation whenever continuous pressure is intended:

- a blocked kick lands into the pivot for a sweep;
- a jump over the sweep lands in the cross-step for a spinning counter;
- a captured limb becomes the lever for a close strike;
- pain-induced folding becomes the path for a counter elbow;
- a blocked hook recovers into a collar tie;
- a wall or vehicle impact becomes the rebound for a final charge.

Do not let performers return to a neutral guard between connected moves. Insert a reset only when distance, advantage, emotion, or geography genuinely changes.

Track support foot, dominant side, attack limb, facing, screen direction, and injury after every beat. Place high-complexity rotation before an injury that would make its takeoff implausible.

## 3. Allocate time and shot density

Choose density from readability and model reliability, not from a house quota.

- Use roughly 8–10 shots in 15 seconds when full-body mechanics, identity continuity, or complex contacts need room.
- Use roughly 12–16 shots only when each short shot carries one clear information slice and the target model has been calibrated for that density.
- Let a shot contain several micro-actions only when they form one causal beat, such as attack → block → landing into the next preparation.
- Protect preparation, contact, and consequence. Do not spend more time on a decorative reaction than on the decisive mechanics.

Empirical starting ranges for normal-speed human action:

```text
simple punch or elbow: 0.2–0.4 s
direct kick: 0.35–0.6 s
complex spinning kick: 0.75–1.0 s
impact or reaction anchor: 0.2–0.5 s
decision close-up: 0.3–0.6 s
```

Treat these as calibration ranges, not guarantees. During a speed-correction pass, remove slow motion entirely before reintroducing one selective time dilation.

## 4. Express speed and force visibly

Use force verbs and acceleration states instead of generic praise:

```text
loads → bursts → whips → strikes → stops → displaces → rebounds
```

For every decisive impact, provide at least three visible layers:

1. source: support foot pressure, hip or shoulder rotation, torso compression;
2. contact: tissue, garment, armor, fur, or surface deformation;
3. transfer: target displacement, delayed torso or head motion, loss of balance;
4. environment: dust, snow, glass, metal, furniture, water, or debris response;
5. residual motion: hair, fabric, tail, breath, fragments, or reverberation continuing after the body stops.

Write the speed curve directly: very short preparation, rapid acceleration, peak speed immediately before contact, hard deceleration at contact, immediate consequence. Keep the torso, support foot, and contact point readable while allowing directional blur on fast limbs and foreground particles.

## 5. Motivate action camera movement

Let action trigger the camera. Define start cue, travel, arrival, and hold.

| Action event | Useful response | Required landing |
|---|---|---|
| sudden charge or commitment | short push | settle before decisive contact |
| lateral kick, chase, or knockback | lateral track | preserve full-body silhouettes and axis |
| vertical lift, jump, or descending strike | tilt | stop where height and target are both readable |
| strong knockback or revealed destruction | fast pull | arrive on the changed distance and environment |
| dominance reversal around joined bodies | short arc on one side of the axis | stop before the strike lands |
| impact | one brief impulse | recover immediately |
| redirected limb or foreground occlusion | whip pan | land on a precise subject or complete the transition |

Use one primary camera move per shot. Do not combine performer rotation with automatic camera orbit. For a spinning kick, prefer a stable three-quarter medium-wide or full-body view; let the performer create the arc.

Use over-the-shoulder framing for anticipation or pressure, not for proving full-body contact. Keep the foreground shoulder small enough that it does not distort body scale or hide the attack path.

## 6. Protect identity and body proportions

Label each reference by purpose: identity, face, full body, costume, pose, environment, lighting, or mood.

When a character sheet contains large face close-ups above smaller full-body views:

- state that the layout and relative image sizes are not character proportions;
- use a clean full-body crop as the primary proportion reference when possible;
- use the face crop only as a secondary identity reference;
- avoid close, wide-angle over-the-shoulder action coverage;
- return regularly to full-body or medium-wide proportion anchors.

If the model preserves the face but compresses the torso and limbs, first correct reference hierarchy, lens distance, and shot complexity. Do not rely only on a long negative prompt.

When footwear is continuity-critical, lock its silhouette, heel height, sole, material, and contact behavior. For stylized action in narrow high heels, place explosive takeoff and rotation on a stable hard or compacted surface, drive through the forefoot, let the heel skim or settle after the pivot, and do not make the heel tip carry torsional load. Keep the footwear visible at key takeoff and landing beats; forbid morphing into flat shoes, broken heels, floating feet, or twisted ankles. Treat this as screen-direction logic, not a safe real-world stunt prescription.

## 7. Handle rotations, chases, and environmental impacts

### Rotations

Show the takeoff foot, rotation axis, attack limb, target, contact, and landing or capture. State which foot drives and which limb attacks. Keep the camera stable during the fastest rotation. Do not use slow motion merely to display costume motion.

### Chases and parkour

Preserve route, leader, trailing distance, takeoff point, landing order, and screen direction. Aerial attacks must follow from established velocity and must end in a readable landing or collision state.

### Environmental impacts

Use the environment as evidence and as the next tactical resource. Specify the first material to deform, secondary vibration or fracture, debris direction, performer rebound, and the new attack opportunity. Avoid generic destruction with no effect on blocking.

## 8. Write the compact model prompt

Use this order:

```text
[FORMAT]
Duration, aspect ratio, output cadence, reality level, dialogue or subtitle rule.

[REFERENCE AND CONTINUITY LOCK]
Character identity, full-body proportions, costume, footwear, geography, screen direction, incoming injuries.

[VISUAL LOCK]
Camera family, lens range, light direction, palette, weather, surface behavior.

[SHOT]
Timecode | framing and lens | one camera behavior.
Incoming state → trigger → action → defense → contact → consequence → outgoing state.
Sound bridge or impact cue.

[TARGETED NEGATIVES]
Only observed or high-probability failures.
```

Keep each shot centered on one dominant beat. Prefer observable verbs over explanatory phrases. Repeat an invariant only at a drift-prone transition.

## 9. Diagnose common failures

| Failure | Likely cause | First correction |
|---|---|---|
| action feels slow | long preparation, repeated reaction prose, slow-motion language, or too few micro-actions | shorten preparation; remove slow motion; connect recovery to the next attack |
| hits lack force | contact described without source, transfer, or consequence | add support-foot drive, hard contact stop, displacement, and environment response |
| moves feel disconnected | every move begins from neutral | make the outgoing pose and momentum seed the next move |
| camera feels flat | every shot is fixed without contrast | add a few action-triggered pushes, tracks, pulls, or whip pans with stable arrivals |
| camera feels synthetic | continuous float, orbit, or simultaneous movements | assign one motivated move and a hold; let performer movement provide energy |
| head appears too large | face-dominant reference sheet, close wide lens, foreground head, or anatomy drift under complexity | prioritize full-body reference; increase camera distance; simplify the shot |
| spinning move floats | rotation plus camera orbit, slow motion, or missing takeoff and landing | use a stable full-body angle; show drive foot, axis, contact, and recovery |
| injury disappears | state not carried into later support and attack choices | restate the injured limb at each weight-bearing or force-producing beat |
| prompt loses priority | internal labels, duplicated rules, and long collaborator explanations | translate labels into visible behavior and compress repeated constraints |

## 10. Audit

```text
[ ] Every exchange has an objective and changes advantage, distance, damage, or geography.
[ ] Every connected move begins from the previous outgoing state.
[ ] Support feet, attack limbs, and screen direction remain consistent.
[ ] Complex rotations have readable takeoff, axis, target, contact, and recovery.
[ ] Every decisive hit shows source, contact, transfer, and consequence.
[ ] Camera movement is triggered by action and has a stable arrival.
[ ] Full-body anchors protect proportions and contact mechanics.
[ ] Slow motion is selective and causally necessary.
[ ] Injuries change later balance, speed, and tactical choices.
[ ] The final model prompt contains observable instructions, not unexplained internal style names.
```
