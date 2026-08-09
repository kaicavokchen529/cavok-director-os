# AI Video Model Adapters

## Principle

Keep directing intent model-independent. Convert it into a model-specific execution plan only after confirming the exact model, version, interface, duration limits, reference inputs, audio support, and current documented capabilities.

Do not assume current product behavior from memory. Verify official documentation or the active interface when model features may have changed.

## Capability probe

Record:

- model and version;
- text-to-video, image-to-video, reference, extension, edit, and audio modes;
- allowed duration, aspect ratio, resolution, frame rate, and output count;
- reference-image count and identity controls;
- camera-control syntax or UI controls;
- negative-prompt behavior;
- seed, variation, region editing, first/last frame, and clip-extension support;
- content-policy and upload constraints.

## Adaptation decisions

Choose:

- maximum beats per generation;
- whether to generate one shot, a short sequence, or a transition;
- which details belong in text versus reference media;
- whether dialogue and audio are generated together or in post;
- whether continuity is driven by first frame, last frame, character reference, or external compositing;
- how much camera language the model follows reliably;
- which internal style terms must be translated into observable behavior;
- the shortest prompt that preserves identity, causal action, camera, and continuity;
- which negatives are effective and which create prompt competition.

## Stable adapter record

```text
Model / version / date checked:
Official capability source:
Supported inputs and outputs:
Reliable shot complexity:
Identity strategy:
Camera strategy:
Audio strategy:
Prompt structure:
Known failure patterns:
Recommended split points:
Retry strategy:
```

## Controlled calibration

Before a costly scene, run a short test matrix that changes one variable at a time: identity reference, shot duration, camera movement, action count, VFX density, and prompt length. Promote observations into the adapter only after repeated evidence. Label undocumented behavior as empirical, not guaranteed.

Do not assume that a model recognizes a project-specific style name. Keep that name in the director layer and express its intended timing, movement, contact, and image behavior directly in the execution prompt unless controlled tests prove the token is useful.

Never let adapter constraints silently alter story logic. Report when the directing plan must be split, simplified, or executed through compositing.
