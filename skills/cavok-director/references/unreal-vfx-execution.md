# Unreal Engine VFX Execution

## Contents

1. Placement in the directing pipeline
2. System ownership
3. Chaos execution
4. Niagara execution
5. Lumen execution
6. Sequencer and orchestration
7. Shot parameter template
8. Validation and performance

## 1. Placement in the directing pipeline

Use this reference only when the target is Unreal Engine or when the user requests engine-ready technical direction. Keep implementation parameters out of model-agnostic prompts.

Translate the scene in this order:

```text
Directorial intent
→ physical VFX event design
→ Chaos object and force simulation
→ Niagara visible media and particles
→ Lumen lighting and reflection integration
→ Sequencer timing and camera synchronization
```

Define the physical event in `cinematic-vfx.md` before selecting engine systems. Do not let a tool determine the dramatic design.

## 2. System ownership

Assign each observable consequence to one primary system:

| Requirement | Primary system | Typical examples |
|---|---|---|
| Rigid objects break, collide, fall, or receive force | Chaos | ice fracture, branches, rocks, debris |
| Cloth, hair, flesh, or physical animation responds | Chaos family | coat recoil, hair impulse, body recovery |
| Fine visible media forms, flows, and dissipates | Niagara | flame, vapor, frost dust, sparks, ash |
| Dynamic indirect light and reflections update | Lumen | fire bounce, wet ground reflection, ice reflection |
| Effect beats synchronize with performance and camera | Sequencer | charge, release, contact, hold, dissipation |
| Systems exchange triggers or data | Blueprint / data interfaces | collision event spawning steam and particles |

Avoid duplicating the same motion in Chaos and Niagara. Use Chaos for simulation-authoritative large fragments and Niagara for fine fragments or non-authoritative visual detail.

## 3. Chaos execution

Use Chaos in the **contact, physical feedback, secondary reaction, and aftermath** stages.

### Define simulation intent

Specify:

- simulated object and collision representation;
- mass, center of mass, inertia, friction, restitution, gravity, drag, and damping;
- fracture hierarchy and cluster behavior;
- damage threshold or strain required at each fracture level;
- impact point, force direction, radius, falloff, duration, and field type;
- initial velocity, angular velocity, collision filtering, sleep, and removal behavior;
- whether the shot needs deterministic cache playback.

Use Geometry Collections for authored destruction. Place denser fracture detail near likely contact areas and keep large readable pieces in the silhouette. Use Physics Fields to localize strain, velocity, force, or disable/sleep behavior.

### Preserve cinematic causality

Trigger fracture at the visible contact frame. Make fragment velocity inherit both the object's incoming momentum and the collision force. Keep large fragments physically authoritative; let small fragments lose energy faster. Do not produce omnidirectional debris when the force is directional.

For repeatable cinematic shots, simulate, approve, and cache the result before final lighting and render. Recheck penetrations, premature fracture, weightlessness, excessive bounce, and fragments crossing faces or the camera.

### Example: ice spear fracture

```text
Asset: GC_IceSpear
Contact driver: localized strain field at impact point
Fracture: medium structural pieces plus fine contact-region detail
Velocity: forward spear momentum plus lateral steam pressure
Material response: brittle fracture, low bounce, limited sliding
Aftermath: large fragments remain physical; fine fragments transition to Niagara
```

## 4. Niagara execution

Use Niagara in the **precursor, formation, propagation, secondary effect, and dissipation** stages.

Build one Niagara System for the complete effect and separate materially distinct behaviors into emitters. A collision system may contain emitters for dense contact steam, fine ice, sparks, heat distortion, displaced leaves, and residual mist.

### Parameter groups

Expose shot controls rather than burying values inside modules:

```text
Timing
- start time, spawn rate, burst count, lifetime, loop behavior

Shape
- source position, source radius, cone angle, bounds, attachment space

Motion
- initial velocity, directional bias, drag, curl noise, vortex, gravity

Appearance
- size curve, opacity curve, color/temperature, roughness, emissive intensity

Interaction
- collision mode, restitution, friction, kill/stick/slide response

Quality
- CPU/GPU simulation, fixed bounds, LOD, significance, cull distance
```

Use mesh particles for visible fragments and sprites or volumes for fine media. Prefer GPU simulation for large non-authoritative particle counts; use CPU simulation when accurate event generation or gameplay-grade collision data is required. Set fixed bounds deliberately so the system does not disappear at frame edges.

### Drive material behavior

Use Niagara parameters to drive dynamic material inputs such as temperature, opacity, distortion, erosion, and emissive intensity. Make curves reflect the effect lifecycle rather than linear fade-ins and fade-outs.

### Connect Chaos and Niagara

Use collision, fracture, or Blueprint events to pass contact position, normal, impulse, fragment velocity, and material identity into Niagara user parameters. Spawn vapor at the actual thermal contact region, not at the asset origin.

## 5. Lumen execution

Use Lumen in the **lighting interaction, material integration, and final-look** stages.

### Project and shot decisions

Record:

- Lumen Global Illumination and Lumen Reflections state;
- software or hardware ray tracing path;
- target platform and frame budget;
- Post Process Volume quality overrides;
- Surface Cache or reflection issues visible in the shot;
- translucent, foliage, water, and emissive-material requirements.

Choose hardware ray tracing when the shot requires the highest-quality mirror-like or geometry-accurate reflections and supported hardware is available. Use software ray tracing when scalability and scenes with many overlapping instances make it the practical option.

### Integrate emissive effects safely

Do not rely on a tiny, extremely bright Niagara sprite to provide stable scene lighting. Small intense emissive sources can become noisy or fail to produce the desired indirect response.

Use this division:

- Niagara material: visible flame core, tongues, sparks, and distortion;
- local movable light: stable direct interaction on faces, fabric, trees, and ground;
- Lumen: diffuse bounce, indirect shadowing, and reflections;
- Sequencer: animate intensity, radius, temperature, and falloff with the effect lifecycle.

Keep daylight fire interaction local. Do not turn a sunlit forest into orange night. Render ice primarily through transparent material response, environmental reflection, refraction, cracks, inclusions, and specular edges rather than blue emission.

### Diagnose Lumen artifacts

Inspect Lumen visualization modes and compare Screen Traces against the fallback representation. Check Surface Cache coverage, mesh distance fields when using software tracing, material roughness, emissive source size, reflection method, and update latency before raising global quality.

## 6. Sequencer and orchestration

Create explicit timing markers:

```text
T0 precursor
T1 formation begins
T2 release
T3 first contact
T4 peak physical reaction
T5 secondary debris and media
T6 dissipation begins
T7 stable aftermath
```

Synchronize:

- character animation and gaze;
- Chaos field activation or cached simulation;
- Niagara activation and user parameters;
- local interaction-light curves;
- exposure and focus behavior;
- camera shake only at force arrival;
- sound transients and environmental tails.

Do not shake the camera before the pressure wave reaches it. Preserve a readable hold after the peak so the audience can perceive consequence.

## 7. Shot parameter template

```text
Shot / frame range:
Target platform / frame rate / render path:
Physical event and dramatic purpose:

Chaos
- assets and collision:
- mass / material behavior:
- fracture / thresholds:
- field type / position / direction / radius / falloff:
- cache strategy:

Niagara
- system and emitter list:
- source and attachment:
- spawn and lifetime:
- velocity / forces / collision:
- size / opacity / material curves:
- bounds / simulation target / scalability:

Lumen and lighting
- GI / reflection method:
- ray-tracing path:
- emissive contribution:
- direct interaction lights:
- reflection / translucency / foliage requirements:
- Post Process Volume overrides:

Sequencer
- trigger markers:
- parameter curves:
- camera / focus / shake synchronization:
- sound synchronization:

Validation
- causality:
- material and lighting integration:
- collision and penetration:
- temporal stability:
- GPU / game-thread budget:
```

## 8. Validation and performance

Validate in this order:

1. Confirm the dramatic beat and contact frame.
2. Check Chaos scale, mass, force direction, fracture, and collision.
3. Check Niagara spawn origin, lifecycle, bounds, collision, and overdraw.
4. Check local direct light before tuning Lumen indirect response.
5. Inspect Lumen scene, reflection, and Surface Cache diagnostics.
6. Profile GPU and simulation cost at target resolution and scalability.
7. Cache expensive deterministic simulations for final cinematic output.
8. Review the final render for flicker, noise, popping, clipping, temporal trails, and mismatched dissipation.

Tune the cheapest responsible layer. Do not raise global Lumen quality to hide a bad material, add particles to hide weak Chaos motion, or increase destruction complexity when the shot cannot resolve it.

