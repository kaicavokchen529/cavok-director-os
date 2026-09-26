# Cinematography Language Engine

## Purpose and authority

Use this module as the single authority for scene-level cinematography strategy and camera-language selection. It decides **how the audience is allowed to see**, how visual distance evolves, which camera platform and optical behavior belong to the scene, when expressive techniques enter the candidate pool, and how one camera regime hands off to another.

This module selects the camera language. `camera-shot-decision-system.md` refines framing and camera position, `camera-movement-grammar.md` executes movement curves, `camera-optics-sensor.md` defines optical behavior, and medium/model adapters translate the approved design without replacing it.

It must not force a special technique merely to create variety. Its job is to prevent silent fallback to safe third-person coverage while keeping every expressive choice causal, spatially valid, and appropriate to the medium.

## Contents

1. Camera Language Brief
2. Seven independent camera dimensions
3. Viewpoint regimes
4. Visual-distance and shot-size arc
5. Camera position, orientation, and roll
6. Support and operating platforms
7. Optical and focus language
8. Movement topology and angle transitions
9. Temporal camera language
10. Candidate generation and selection
11. Sequence memory and anti-stereotype control
12. Shot execution contract
13. Viewpoint and platform handoffs
14. AI-video translation
15. Cinematography QC

## 1. Camera Language Brief

Before designing individual shots, create a compact internal brief:

```text
Audience relationship:
Viewpoint baseline:
Viewpoint arc:
Scene camera temperament:
Expression permission: L0 / L1 / L2 / L3
Visual-distance curve:
Preferred support palette:
Optical palette:
Spatial movement palette:
Temporal behavior palette:
Special-technique opportunities:
Hero camera event, if any:
Handoff plan:
Repeated defaults to avoid:
End-state camera relationship:
```

### Camera temperament

Choose behavior, not a fixed package:

- **restrained observer:** bodies and blocking alter the frame; camera moves rarely;
- **delayed reactor:** subject moves first; operator catches up, corrects, or chooses not to follow;
- **attached companion:** camera travels with a character while retaining independent attention;
- **predatory controller:** camera anticipates routes, compresses exits, or holds threatening distance;
- **embodied witness:** operating shows footsteps, avoidance, breath, imbalance, or physical proximity;
- **ritual observer:** symmetry, measured moves, stable horizons, deliberate reveals;
- **exploratory presence:** movement discovers layered space and changing relationships;
- **graphic or impossible observer:** stylized 2D/CG camera prioritizes pose, vector, transformation, or visual metaphor.

Temperament guides responses across the scene. It does not prescribe one support or movement.

### Expression permission

- **L0 — objective:** restrained position changes, stable support, minimal optical intervention;
- **L1 — natural cinematic:** dolly, slider, Steadicam, controlled handheld, motivated focus or zoom behavior;
- **L2 — expressive photographic:** Dutch angle, crash zoom, dolly zoom, Snorricam, extreme positions, conspicuous platform changes;
- **L3 — graphic / virtual:** FPV-like impossible proximity, stylized pass-through, radical perspective, animated camera abstraction, nonhuman POV.

Choose the level from medium, tone, scene function, and approved project law. Do not infer L2–L3 from the word “cinematic.”

## 2. Seven independent camera dimensions

Never collapse all camera design into “movement.” Decide these dimensions separately:

1. **Viewpoint regime:** whose access, knowledge, and body position govern the shot.
2. **Visual distance / shot size:** how close the audience feels and what information remains visible.
3. **Position / orientation / roll:** world-space location, height, side, yaw, pitch, horizon, and Dutch angle.
4. **Support / operating mode:** tripod, dolly, Steadicam, handheld, crane, drone, FPV, body rig, vehicle rig, virtual camera.
5. **Optical behavior:** field of view, focus, zoom, distortion, shutter, filtration, breathing, split focus.
6. **Movement topology and time curve:** line, arc, rise, dive, orbit, pursuit, retreat, pass-through, acceleration, correction, settle.
7. **Temporal behavior:** real time, undercrank/overcrank, speed ramp, bullet time/time slice, freeze or temporal discontinuity, including entry and return to normal time.

A shot may be unusual in one dimension and restrained in the others. Avoid stacking Dutch angle, crash zoom, violent handheld, orbit, and focus whip in one shot unless the scene deliberately enters an extreme perceptual state.

## 3. Viewpoint regimes

### Objective observer

Camera remains outside any one character's perception. Use for geography, evidence, relationship comparison, ensemble action, irony, or consequence.

### Attached third person

Camera travels with one character but can look beyond them. Preserve shoulder, back, profile, route, or environmental relation. Use for exploration, pursuit, investigation, and continuous blocking.

### Semi-subjective

Camera approaches eye or shoulder position while retaining a body edge, weapon, hand, reflection, or nearby physical anchor. Use when embodiment matters but pure POV would lose identity or geography.

### First person / embodied POV

Treat camera as a body, not a flying lens. Define:

- eye/head height and body orientation;
- gaze-led pan/tilt, not frictionless translation;
- footsteps, breath, head stabilization, hesitation, and recovery;
- visible hands, body edge, weapon, vehicle, reflection, or environmental contact when appropriate;
- occlusion, focus search, blinking or exposure response only when justified;
- information limited to what the character can actually perceive;
- physically legible falls, impacts, crouches, turns, and rises.

Do not use first person merely as a novelty insert. It must change knowledge, vulnerability, agency, speed, or bodily pressure.

### Omniscient / aerial

Camera is not owned by a single character. Use to reveal terrain, routes, formations, isolation, encirclement, scale, or system-level consequences.

### Nonhuman or object POV

Camera may belong to surveillance, a vehicle, drone, creature, weapon, projectile, machine, reflection, doorway, or supernatural sensor. Establish its physical or graphic rules and information limits. Do not present an arbitrary unusual angle as POV without an owner or governing system.

### Viewpoint arc

A scene may evolve through regimes, for example:

```text
omniscient aerial
→ attached third person
→ semi-subjective pressure
→ first-person rupture
→ objective consequence
```

Every transition must change audience access or bodily relation and must preserve direction, target, speed, and scene state.

## 4. Visual-distance and shot-size arc

Design the audience-distance curve across the scene before assigning every shot.

Shot size must solve one or more functions:

- geography and route;
- relationship and power;
- full-body mechanism;
- decision and recognition;
- sensory or causal detail;
- impact readability;
- consequence and changed space.

Do not mechanically cycle wide → medium → close → insert → wide. Valid alternatives include:

- refusing to approach a character during their most emotional moment;
- cutting from close proximity to a remote wide to expose isolation;
- holding medium distance so the body, not the face alone, carries performance;
- using full-body contact rather than an impact close-up;
- maintaining oppressive close coverage until one deliberate spatial release;
- returning to geography after a subjective or abstract passage.

For every shot-size change, state internally what new information, relationship, mechanism, or consequence becomes readable. “Variety” is not sufficient.

## 5. Camera position, orientation, and roll

Choose position inside one persistent world. Define camera side, height, distance, facing, foreground, expected background, horizon, and occlusion before lens attribution.

### Dutch angle / roll

Treat roll as a state transition:

```text
level horizon
→ dramatic trigger
→ roll direction and degree appropriate to the shot
→ held or evolving imbalance
→ recovery, escalation, or cut logic
```

Use for perceptual rupture, asymmetric power, unstable physical orientation, abnormal space, or deliberate graphic tension. Do not activate it from “danger” or “villain” alone. Decide whether the character, environment, or both appear unstable.

Extreme high, low, overhead, ground-level, under-object, reflected, obstructed, or split-level positions require a narrative and spatial function. Unusual position is not automatically unusual viewpoint.

## 6. Support and operating platforms

Select support as expressive behavior, not metadata.

| Platform | Strength | Required behavior / constraint |
|---|---|---|
| Tripod / locked | observation, inevitability, performance authority | composition must evolve through blocking or information |
| Dolly / slider | controlled geometry and distance change | define track, start, speed curve, stop, and subject relation |
| Steadicam | fluid human-carried continuity through complex blocking | stable but embodied; allow route negotiation, slight lag, and reframing |
| Gimbal | highly stabilized following or constrained-space movement | avoid frictionless robotic float; define operator path and inertia |
| Handheld / shoulder | embodied uncertainty, proximity, crisis, reactive capture | shake follows footsteps, breath, avoidance, correction, or impact; no random vibration |
| Crane / jib / Technocrane | vertical reveal, scale shift, relationship between levels | tie elevation to information, blocking, or spatial transformation |
| Conventional drone | macro geography, route, formation, sustained travel | define altitude, direction, parallax, spatial fact, arrival, and exit |
| FPV drone / 穿越机 | high-speed proximity, dive, gap traversal, pursuit, spatial threading | define a flyable route, clearance, obstacle order, roll/pitch events, subject reacquisition, and handoff |
| Cable cam | repeatable high-speed line across terrain, crowd, arena, or drop | respect a plausible cable corridor or clearly virtual equivalent |
| Vehicle rig | relation between vehicle, road, occupants, and pursuit | define mount position or independent chase relation |
| Body rig / Snorricam | subject remains stable while world rotates or shifts around the body | reserve for altered bodily state, panic, intoxication, impact, or forced subjectivity |
| Helmet / chest / weapon rig | embodied POV with a visible physical anchor | preserve body mechanics and attachment limitations |
| Surveillance / fixed device | limited access, institutional gaze, evidence | preserve device position, optics, frame rate, and occlusion logic |
| Virtual camera | impossible but designed CG/animation movement | define medium permission, spatial path, inertia, and why physical limits are exceeded |

Do not default scale to drone, intimacy to handheld, or continuity to Steadicam. These are candidates only when the support changes meaning or execution.

### Aerial distinctions

- **high aerial:** map terrain, formation, route, isolation, or aftermath;
- **mid/low aerial:** accompany sustained travel while keeping route and destination readable;
- **vertical descent/ascent:** connect system scale to individual consequence or reverse that relation;
- **top-down graphic view:** reveal pattern, entrapment, order, surveillance, or choreography;
- **FPV traversal:** create speed through near obstacles and route complexity, not merely a faster establishing shot.

## 7. Optical and focus language

Optical change and physical camera travel are different axes.

### Zoom family

- **slow optical zoom:** accumulating attention, surveillance, unease, or perceptual narrowing while camera position remains fixed;
- **crash zoom / snap zoom:** abrupt recognition, target confirmation, tonal punctuation, or stylized action emphasis;
- **dolly zoom:** subject scale remains relatively stable while background perspective changes through coordinated travel and zoom; reserve for genuine spatial or perceptual rupture.

Describe the visible result. Do not use “zoom” as a substitute for an unspecified push-in.

### Focus and depth tools

- rack focus transfers information, agency, or threat between planes;
- deep focus sustains simultaneous conflict;
- split diopter or designed split focus holds separated planes when their relationship matters;
- focus search, lag, or miss may express live operating or embodied perception when motivated.

### Distortion and specialist optics

Use ultra-wide proximity, long-lens compression, macro/probe views, fisheye, filtration, shutter stress, or anamorphic behavior only when their perceptual effect supports the scene and remains consistent with the medium.

## 8. Movement topology and angle transitions

Do not treat “camera movement” as one generic choice. Place every move in a topology family, then define its dramatic trigger, physical or virtual support, speed curve, landing, and exit. Detailed curve execution belongs to `camera-movement-grammar.md`.

### Static, corrective, and reframing

- **locked hold:** blocking, focus, light, or environment changes inside a fixed frame;
- **reframe / correction:** pan, tilt, or small translation responds after attention or body position changes;
- **delayed catch-up:** subject temporarily escapes ideal composition before the operator reacquires;
- **intentional refusal:** camera does not follow, allowing departure, collision, or consequence to occur at the frame edge or offscreen.

### Axial approach and retreat

- **push-in / dolly in:** physically reduces camera-to-subject distance and changes parallax;
- **crash-in / 急推:** rapid physical axial advance triggered by recognition, attack commitment, spatial breach, or irreversible decision;
- **pull-out / dolly out / 后拉:** physically increases distance to release pressure, expose context, or change audience allegiance;
- **reverse pull:** retreats against an advancing subject, force, or consequence while preserving its vector;
- **pull-back reveal:** begins on a detail or restricted relation and withdraws to expose the larger truth;
- **axial retreat:** camera yields along the subject's line of advance, often slower or faster than the subject to control scale growth.

Do not confuse a crash-in with a crash zoom, or a physical pull-out with a zoom-out. State whether perspective and parallax change.

### Lateral, diagonal, and depth movement

- **truck / lateral track:** crosses parallel to subjects and creates foreground/background parallax;
- **parallel follow:** sustains travel direction without changing psychological distance;
- **diagonal converge/diverge:** changes both side relation and distance;
- **foreground reveal/conceal:** translates behind architecture, bodies, vehicles, vegetation, or props;
- **depth pursuit:** travels into or out of screen depth rather than flattening action into side view;
- **crossing pass:** subject, object, or environment passes close to lens and may motivate a handoff or hidden cut.

### Rotational and angular movement

- **pan / whip pan:** redirects attention horizontally; a whip requires a source target, destination target, directional continuity, and readable settle;
- **tilt / whip tilt:** redirects vertical attention or tracks rise/fall;
- **arc:** changes relational angle while retaining a partial side relationship;
- **orbit:** circles a subject or group only when spatial, relational, or ritual transformation benefits from sustained angular change;
- **roll:** changes horizon state; define trigger, direction, peak, hold, and recovery;
- **pivot/reverse look:** turns from one vector or information field into another without pretending the camera translated.

### Vertical and elevation movement

- **pedestal / boom:** changes camera height while largely preserving floor position;
- **crane/jib rise or descent:** connects levels, reveals scale, or transfers attention between system and individual;
- **vertical dive / drop:** rapidly descends with a falling, diving, or discovered subject;
- **ground-skim rise:** begins near contact level and lifts into body or geography;
- **overhead transition:** evolves from oblique or eye-level space into a top shot so orientation change is visible;
- **top-shot descent/ascent:** moves toward or away from a true overhead relation while protecting screen direction.

### Angle and elevation states

Angle is not movement. A shot may hold or travel within any state:

- **high angle / 俯拍:** camera looks downward from above eye level; can expose pattern, vulnerability, route, hierarchy, or restricted agency;
- **true overhead / bird's-eye / 顶拍:** optical axis approaches perpendicular to the ground; useful for graphic choreography, entrapment, evidence, spatial systems, or body placement;
- **low angle / 仰拍:** looks upward to alter scale, authority, threat, architecture, or bodily effort;
- **ground-level / worm's-eye:** camera is close to the support surface and requires foreground/contact logic;
- **under-object / underslung:** camera occupies a physically or graphically justified space beneath action or structure;
- **oblique high/low:** combines elevation with lateral perspective to retain depth better than a pure top shot.

For high-angle and overhead shots, define what becomes newly readable and how the sequence enters and exits the elevated orientation. “俯拍更有电影感” is not a reason.

### Compound and transition moves

Whip pan, roll, orbit, reverse pull, body pass, weapon pass, ground skim, camera crash-in, axial subject rush with yielding retreat, perspective handoff, hidden cut, shot-inside-shot, push-to-stop, and pull-back reveal enter the candidate pool when activation and exit conditions are explicit. Combine moves only when one continuous causal line connects them.

## 9. Temporal camera language

Time treatment is a directing decision distinct from camera speed and shutter behavior. Define **subject time**, **camera time**, **environment time**, and **audio time** separately, then design entry, sustained state, and exit.

### Real-time variants

- **real time:** default causal duration; do not label it unless contrast matters;
- **undercrank / accelerated action:** shortened apparent duration and increased kinetic urgency; protect contact readability;
- **overcrank / slow motion:** expanded duration for decision, mechanism, performance, impact, or consequence—not automatic spectacle;
- **speed ramp:** visible transition between rates tied to a precise action or information event; define start rate, trigger, peak/slow rate, and return point.

### Bullet time / time slice

Bullet time is not merely slow motion. It separates camera travel from subject/world time so the audience can inspect an otherwise inaccessible spatial or causal instant.

Use only when the frozen or near-frozen interval reveals at least one of:

- an attack path, projectile relation, collision chain, or escape gap;
- simultaneous reactions distributed through space;
- a decisive perception or impossible-to-read mechanism;
- a transformation state whose spatial structure matters;
- a deliberate graphic icon that carries narrative weight.

Define:

```text
Entry trigger and exact frozen/expanded instant:
Subject time rate:
Environment/particles/fabric time rate:
Camera route, support permission, and parallax:
What new spatial or causal fact becomes readable:
Audio treatment:
Exit trigger and continuity state on return:
```

Valid forms include a short inspection arc, lateral time-slice, axial pass, overhead inspection, multi-subject spatial reveal, or virtual-camera traversal. Do not use a generic 360-degree orbit by default. Preserve projectile, debris, hair, cloth, expression, and body mechanics consistently at the selected time rate.

### Freeze and temporal discontinuity

- **freeze frame:** editorially arrests an image; distinguish it from a world that is physically frozen while the camera moves;
- **stutter / sampled time:** intentionally drops or repeats temporal samples for rupture, memory, surveillance, or impact;
- **temporal match:** cuts across different moments while preserving composition, motion vector, or pose;
- **subjective time dilation:** one character's perception expands while external causality remains coherent.

Avoid time effects when they weaken force transfer, make geography ambiguous, erase performance rhythm, or conflict with a project rule such as “no slow motion.”

## 10. Candidate generation and selection

For any scene with meaningful cinematography choices, generate three internal candidates for the scene or major beat:

1. **objective / safe:** clearest geography, performance, and continuity;
2. **performance-led:** camera behavior grows from actor blocking, attention, or force;
3. **expressive:** considers viewpoint shift, unusual support, optical intervention, extreme position, aerial/FPV route, or a designed platform handoff.

Each candidate must define the seven camera dimensions. Compare them by:

- dramatic and informational gain;
- character and viewpoint truth;
- spatial legality and continuity;
- performance readability;
- fit with the scene camera temperament;
- relation to preceding and following shots;
- novelty versus meaningful motif;
- medium and production feasibility;
- AI execution risk and available segmentation strategy.

Select one or combine only compatible parts. Do not show the candidate set unless the user asks. If the expressive candidate is rejected, reject it for a specific reason rather than silently defaulting to safe coverage.

## 11. Sequence memory and anti-stereotype control

Track recent camera choices across the sequence:

- viewpoint regime;
- shot size and subject occupancy;
- height, side, and roll;
- support/operating mode;
- optical behavior;
- movement topology and direction;
- temporal behavior and rate transition;
- trigger type;
- start and end composition;
- contact or consequence behavior.

Check for automatic repetition:

- every emotional increase becomes a push-in;
- every action launch becomes a following track;
- every climax becomes an orbit;
- every impact becomes shake;
- every scale beat becomes drone;
- every tense beat becomes handheld or Dutch;
- every major impact becomes slow motion, speed ramp, or bullet time;
- every urgent beat becomes a crash-in and every consequence becomes a pull-out;
- every overhead angle becomes a rotating top shot;
- every move starts before the subject and lands perfectly;
- every scene remains safe third person;
- every shot changes technique merely to avoid repetition.

Repetition is valid when it is a motif. A repeated camera behavior must preserve, reverse, fail, intensify, or meaningfully break its earlier function.

## 12. Shot execution contract

For every conspicuous shot, define:

```text
Shot function:
Viewpoint regime and owner:
Start composition and subject occupancy:
World-space position, height, side, horizon/roll:
Support / operating mode:
Lens / optical behavior:
Character or information trigger:
Camera lead / lag relationship:
Movement path and topology:
Acceleration, correction, and settle:
Temporal behavior, entry, and exit:
Framing evolution:
Focus behavior:
End composition and hold:
Exit / cut / handoff:
Director intent:
```

The start and end compositions matter as much as the named move. A camera move without a designed landing is incomplete.

## 13. Viewpoint and platform handoffs

Use handoffs to create a camera-language arc rather than isolated tricks.

Possible handoffs:

- drone high aerial → lower route-follow → ground camera;
- FPV traversal → vehicle or body pass occlusion → Steadicam pursuit;
- objective two-shot → semi-subjective shoulder → first-person rupture;
- first person → impact blackout/occlusion → objective consequence;
- crane descent → foreground wipe → handheld or dolly-level scene entry;
- surveillance feed → matched composition in primary camera;
- physical support → clearly motivated virtual-camera release in stylized CG/animation.

At every handoff preserve or intentionally transform:

- target identity;
- screen and travel direction;
- speed and momentum;
- spatial anchor;
- viewpoint ownership;
- exposure/color/optical state when continuity requires it;
- reason the new platform can now see what the old one could not.

## 14. AI-video translation

Name the technique when useful, then describe observable behavior. Do not rely on labels alone.

- **Steadicam:** human-carried height, fluid route negotiation, slight embodied rise/fall, delayed reframe, no robotic float.
- **Handheld:** bounded operator corrections caused by steps, breath, avoidance, urgency, or impact; no random vibration.
- **Dutch angle:** roll direction, trigger, evolving or held horizon, and recovery/cut logic.
- **Optical zoom:** camera position remains fixed; framing changes without dolly parallax.
- **Crash-in / 急推:** camera physically advances on axis with rapidly increasing subject occupancy and changing parallax; define trigger, peak speed, braking, and landing.
- **Pull-out / 后拉:** camera physically retreats with widening geography and changing parallax; define whether subject advances, holds, or recedes independently.
- **High angle / overhead:** state camera height, downward pitch, ground relation, visible pattern, and how orientation is established.
- **Bullet time:** state the selected instant, subject/world time rates, camera route and parallax, suspended secondary motion, audio state, and return-to-time trigger.
- **FPV drone:** altitude, route, obstacle sequence, dive/rise/roll, subject loss/reacquisition, arrival, and handoff.
- **First person:** head/gaze behavior, body anchor, contact, information limit, and physically coherent turns or falls.

If a model cannot execute a complex continuous handoff, split at occlusion, motion blur, darkness, flare, foreground passage, stable framing, or a state boundary. Preserve the approved viewpoint and movement logic across the split.

## 15. Cinematography QC

Before delivery, verify:

- the scene has a camera temperament, viewpoint baseline, and viewpoint arc;
- visual distance changes for information or relationship, not variety alone;
- shot size, position, support, optics, movement, and temporal behavior were selected independently;
- at least one expressive candidate was considered when the scene permits it;
- first-person, aerial, FPV, Dutch, zoom, crash-in, pull-out, overhead, Steadicam, handheld, body-rig, bullet time, speed ramp, or virtual techniques appear when they solve the scene—not only when named by the user;
- any rejected expressive option had a real dramatic, spatial, tonal, or execution reason;
- camera support has observable operating behavior;
- movement has a designed trigger, curve, landing, hold, and exit;
- the sequence does not silently repeat safe third-person coverage;
- unusual techniques do not erase geography, performance, causality, or continuity;
- viewpoint/platform handoffs preserve or deliberately transform target, direction, speed, space, and audience knowledge;
- model adaptation translates the camera design rather than flattening it.
