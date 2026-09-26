# Camera Language Safe-Default Failure

## Symptom

The shot plan is technically clear but repeatedly falls back to eye-level third-person medium coverage, restrained push/pull, generic tracking, and stable action masters. First-person, semi-subjective, Dutch angle, optical zoom, Steadicam, handheld, aerial, FPV, body rig, cable cam, vehicle rig, or designed virtual-camera behavior never enters consideration unless the user explicitly names it.

## Likely causes

- cinematography was selected one shot at a time without a scene-level viewpoint arc;
- safety, continuity, and AI feasibility were treated as the only positive goals;
- special techniques had anti-misuse rules but no activation scan;
- support, optics, position, and movement were collapsed into one generic “camera move” decision;
- the system selected one safe answer before generating an expressive candidate;
- repeated camera choices were not tracked across the sequence.

## Diagnostic questions

- What is the scene's camera temperament and expression permission level?
- Does the scene have a viewpoint arc or remain default third person throughout?
- Were objective, performance-led, and expressive candidates compared?
- Did the plan scan for first-person, aerial, FPV, special optics, unusual position, and platform handoff opportunities?
- Is every support named only as metadata, or does its operating behavior affect the image?
- Are repeated shot sizes, triggers, movement paths, and landings forming an unintended template?

## Fix

Run `cinematography-language-engine.md` before detailed shot design. Build the Camera Language Brief, generate three internal candidates, select the seven camera dimensions independently, and apply the sequence-memory audit. Preserve the safest candidate only when it wins for a stated reason.

## Preventive rule

Safety is a constraint, not the sole creative objective. When a scene permits expressive photography, at least one expressive candidate must enter comparison even if the final choice remains restrained.
