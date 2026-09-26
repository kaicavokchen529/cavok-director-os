# Combat Decision Engine

## Purpose

Use this module as the single authority for tactical action selection in duels, melee, weapon combat, creature encounters, and superpower exchanges. It governs what each fighter can legally attempt, how both sides update their decisions, and how every action changes the fight state.

It does not prescribe named martial arts, fixed combinations, mandatory shot counts, or a platform-specific prompt format. Camera interpretation belongs to `hyperreal-action-direction-v2.md` or `2d-anime-combat-grammar.md`; cross-shot state continuity belongs to `continuity-direction.md`.

## Contents

1. Bind capabilities, not choreography
2. Maintain a tactical state packet
3. Select actions from state
4. Give the opponent agency
5. Apply the action-value gate
6. Use observable state transitions
7. Shape rhythm through decisions
8. Integrate with camera and medium
9. Combat QC

## 1. Bind capabilities, not choreography

Define each fighter's action boundary before composing exchanges:

- immediate objective and loss condition;
- preferred, acceptable, and dangerous ranges;
- legal attacks, defenses, controls, movement options, weapons, and abilities;
- dominant side, stance logic, movement character, and reliable tactical habits;
- costs, cooldowns, recoil, injuries, environmental limits, and failure modes;
- signature decisions that reveal character without fixing an exact sequence.

A capability binding answers **what is plausible for this fighter now**. It must not lock a universal combo order, guaranteed counter, or predetermined ending. If the request introduces an unbound skill, weapon, or ability, mark it as a Director Proposal unless the user approves it.

## 2. Maintain a tactical state packet

At the start of each exchange and after every meaningful action, track only the fields that affect the next decision.

### Geography

- distance band, elevation, orientation, attack lane, exits, obstacles, cover, and hazardous surfaces;
- screen direction and axis only when they affect staging or continuity;
- whether either fighter can actually reach the intended target.

### Body and object state

- facing, stance, support side, center of mass, balance, and current momentum;
- free, occupied, trapped, injured, or committed limbs;
- grip, weapon location, prop ownership, restraint/contact, and recovery state;
- damage, fatigue, ability residue, and environmental interference.

### Tactical state

- current guard and genuinely exposed targets;
- control point, pressure source, escape route, and available counter lane;
- initiative holder, why initiative is held, and what could transfer it;
- immediate threat, current advantage, and unresolved action consequence.

### Information state

- what each fighter has directly observed;
- what pattern each fighter currently suspects;
- what remains unknown or is being deliberately concealed;
- what new evidence would justify an adaptation.

Do not expose the full packet in the user-facing answer unless requested. Use it internally to keep action legal and continuous.

## 3. Select actions from state

Before accepting an action, answer:

1. What tactical objective does it serve now?
2. Is it legal from the current distance, balance, limb, weapon, injury, and momentum state?
3. What opening, pressure, or observed pattern makes this target available?
4. What visible state will change if it succeeds, misses, or is countered?
5. What cost, recovery, or exposure does it create?
6. What credible response remains available to the opponent?
7. Can the audience read the cause and result at the intended speed?

Reject actions that require an invisible reset, impossible reach, duplicated weapon, unsupported ability, ignored injury, or opponent passivity.

## 4. Give the opponent agency

Build exchanges as an evidence-and-adaptation loop:

```text
Probe or committed action
→ opponent observes usable evidence
→ opponent changes guard, distance, timing, route, or objective
→ first fighter recognizes or misses that adaptation
→ exploit, failed exploit, counter, or counter-counter
→ initiative and state update
```

An adaptation must be caused by evidence visible in the exchange. Do not grant mind-reading. Do not repeat the same defense after it has clearly failed unless fear, injury, deception, lack of options, or character choice explains the repetition.

When one fighter dominates, preserve opponent agency through escape attempts, sacrificial defenses, terrain use, delay tactics, information gathering, protection of another objective, or a forced loss decision. Agency does not require equal strength.

## 5. Apply the action-value gate

Keep an action only if it changes at least one of these:

- contact or restraint;
- distance, angle, elevation, or route;
- balance, support, momentum, or facing;
- guard, exposed target, or control point;
- initiative, timing, rhythm, or information;
- weapon, prop, resource, injury, or environment state;
- relationship, objective, escape condition, or ending access;
- audience understanding of character, threat, or consequence.

Delete decorative movement that changes none of them. If deletion breaks continuity, add only the shortest observable transition needed to connect the surrounding states.

## 6. Use observable state transitions

Write each meaningful beat as:

```text
Before state
→ intention and visible tell
→ legal action and opponent response
→ contact, miss, control, or interruption
→ force / information transfer
→ consequence and recovery
→ after state
```

A cut may change viewpoint; it may not perform the physical transition. Standing, falling, drawing, disarming, escaping restraint, changing hands, recovering balance, or crossing an obstacle must occur visibly or be separated by an explicit time/location jump.

## 7. Shape rhythm through decisions

Do not impose a universal number of strikes, counters, cuts, or initiative changes. Build rhythm from variation in:

- decision speed;
- causal depth;
- commitment and recovery;
- initiative duration;
- contact versus near miss;
- compression versus spatial release;
- certainty versus deception;
- action versus consequence.

High density is useful only when state remains readable. A pause must still contain pressure, observation, recovery, concealment, or a decision; otherwise it is empty duration.

## 8. Integrate with camera and medium

After the tactical chain is legal:

- use `hyperreal-action-direction-v2.md` to couple performance, three-dimensional staging, contact, consequence, and camera response in photographed or hyperreal modes;
- use `2d-anime-combat-grammar.md` to translate the same causality into key poses, spacing, smears, impact frames, and consequence poses in 2D/anime modes;
- use `continuity-direction.md` to carry body, object, injury, momentum, and environment states across shots or generated clips;
- let model adapters change syntax and segmentation only, never tactical causality.

## 9. Combat QC

Before delivery, verify:

- every major action is legal from the preceding state;
- capability bindings constrain options without becoming fixed combinations;
- both sides pursue objectives and react to evidence;
- initiative changes have visible causes;
- attacks target actual openings rather than decorative body regions;
- no action survives only to fill time or add spectacle;
- injury, weapon, support, momentum, and control states do not reset invisibly;
- action consequences create the next decision;
- camera or graphic treatment clarifies the tactical event instead of replacing it.
