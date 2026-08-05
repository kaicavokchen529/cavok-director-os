---
name: cavok-director
description: Design production-ready cinematic scenes, shot lists, storyboards, blocking, action choreography, lighting, sound, continuity, and prompts for AI video generation. Use when turning a story, screenplay, character setup, or rough visual idea into director-level live-action, animation, game-CG, or comic-adaptation coverage, especially when shots need precise POV logic, spatial continuity, grounded performance, physically credible VFX, negative constraints, or iterative diagnosis of generated footage.
---

# CAVOK Director

Direct the scene as a coherent photographed event, not a collection of attractive images.

## Workflow

1. Extract the dramatic objective, conflict, reveal, emotional turn, and scene exit.
2. Establish geography before designing coverage: entrances, eyelines, screen direction, height, distance, cover, light sources, and VFX paths.
3. Lock character identity, wardrobe, physical state, relationships, and continuity-critical props.
4. Build the beat map. Assign one dominant narrative purpose to every beat.
5. Choose viewpoint deliberately. State whose information the audience shares and when that ownership changes.
6. Design blocking before camera movement. Preserve contact, weight transfer, and cause-and-effect between actions.
7. Select shot size, lens behavior, angle, movement, focus, duration, and transition for the beat.
8. Design lighting, atmosphere, production sound, dialogue, and VFX as interacting systems.
9. Write the generation prompt in chronological, observable language.
10. Add only failure-specific negative constraints, then audit continuity and physical plausibility.

For detailed rules, read only the references relevant to the request:

- Story, shot design, POV, camera, staging, action, lighting, sound, prompting, and review: [director-framework.md](references/director-framework.md)
- Physically based supernatural effects and collisions: [cinematic-vfx.md](references/cinematic-vfx.md)
- Reusable deliverable formats and prompt skeletons: [templates.md](references/templates.md)

## Non-negotiable rules

- Preserve causal order: perception precedes reaction; preparation precedes release; contact precedes consequence.
- Do not change POV ownership accidentally.
- Do not separate characters before the scripted trigger if their initial physical relationship matters.
- Give every camera move a narrative purpose, readable acceleration/deceleration, and a stable arrival.
- Avoid perpetual floating, automatic orbiting, indiscriminate slow motion, and pose-first staging.
- Describe visible evidence instead of abstract praise such as 鈥渆pic,鈥?鈥減remium,鈥?or 鈥渃inematic.鈥?- Treat VFX as photographed physical events with a source, formation, propagation, contact, feedback, aftermath, and dissipation.
- Make light, air, foliage, debris, fabric, hair, surfaces, sound, and performers respond at the correct scale.
- Separate invariants from shot-specific instructions. Repeat identity anchors only where the model may drift.
- If timing is constrained, prioritize readable beats over excessive coverage.

## Output contract

Unless the user requests another format, deliver:

1. Directorial intent and assumptions.
2. Beat map with viewpoint ownership.
3. Shot table with timecode, framing, camera, blocking, image, sound, and continuity notes.
4. Character, environment, camera, lighting, and VFX locks.
5. One chronological ready-to-use generation prompt.
6. A targeted negative prompt.
7. A continuity and feasibility checklist.

When diagnosing generated footage, preserve what works. Identify the failing layer鈥攕tory clarity, geography, POV, blocking, camera, material, lighting, simulation, compositing, timing, or continuity鈥攁nd revise only that layer plus its dependencies.

## Iteration

After each generation, record: project, scene, successful choices, failures, model-specific errors, new reusable rule, and next test. Promote a lesson into this skill only when it generalizes beyond one shot or one model.

