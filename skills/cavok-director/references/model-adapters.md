# AI Video Model Adapters

## Principle

Keep directing intent model-independent. Convert it into a model-specific execution plan only after confirming the exact model, version, interface, duration limits, reference inputs, audio support, and current documented capabilities.

Do not assume current product behavior from memory. Verify official documentation or the active interface when model features may have changed.

## Adapter routing

When the target model has a dedicated adapter, load it only at the execution layer after the directing plan is stable.

Current dedicated adapters:

- Seedance 2.5: [seedance-2.5.md](seedance-2.5.md)

Inside the CAVOK project, `SD2.5` may be interpreted as Seedance 2.5 when the task is clearly AI video generation. Outside that context, confirm the intended model if the shorthand is ambiguous.

A dedicated adapter may change prompt structure, reference assignment, timestamp strategy, extension/edit wording, and model-specific retry strategy. It must not silently alter story logic, character motivation, geography, action causality, camera motivation, or continuity law.

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

Never let adapter constraints silently alter story logic. Report when the directing plan must be split, simplified, or executed through compositing.
