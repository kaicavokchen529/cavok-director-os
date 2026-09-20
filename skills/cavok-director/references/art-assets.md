# Art and Asset Direction

## Govern visual identity

Create approved bibles for characters, environments, props, creatures, vehicles, materials, VFX motifs, and graphic elements. Record both visual intent and production identifiers.

## Character bible

Include orthographic or multi-angle references, proportions, face anchors, hair structure, wardrobe layers, fabric and wear, accessories, color values, movement restrictions, scale, and forbidden deviations. Separate permanent identity from scene-specific condition.

## Environment bible

Include layout, scale references, entrances, elevations, navigable surfaces, camera access, light sources, weather, vegetation, dressing density, destructible areas, and state changes across the scene.

## Prop and material bible

Record owner, dimensions, handedness, operation, hero side, damage states, reflective properties, roughness, transparency, aging, and continuity location. Define how material behaves under water, frost, heat, dirt, blood, and impact.

## Reference hygiene

Label each reference as identity, costume, pose, lighting, environment, lens, material, VFX, motion, composition, or mood. Do not let a mood reference silently override identity or geography. Record source, license, date, and allowed usage.

## Reference Responsibility Contract

Every production reference must have an explicit responsibility. Reference quantity is not control; ambiguous responsibility creates cross-contamination.

Use a compact contract:

```text
Reference ID:
Use for:
Do not inherit:
Priority / conflict rule:
Version / approval state:
```

Typical responsibilities:

- character reference: identity, face, hair, proportions;
- costume reference: garment structure, material, accessories;
- weapon / prop reference: silhouette, dimensions, handedness, material, operating state;
- environment reference: layout, scale, weather, daylight, material and fixed landmarks;
- VFX reference: color hierarchy, shape language, density, scale and dissipation;
- keyframe / storyboard reference: camera position, pose, blocking, composition or perspective only when specified;
- motion / video reference: timing, trajectory, footwork, camera acceleration, blocking or rhythm only when specified.

If a user says “reference color only,” do not inherit architecture, costume, pose, lighting direction, or other unassigned features from that image. If multiple references conflict, the explicit responsibility and approved version win over visual similarity.

Reference contracts are model-independent. Model-specific adapters may translate them into syntax, but may not broaden a reference's responsibility.

## Naming and versioning

Use stable IDs:

```text
CHAR_Name_Version
ENV_Location_State_Version
PROP_Name_State_Version
VFX_Ability_Beat_Version
SHOT_Sequence_Shot_Take_Version
```

Maintain approved, work-in-progress, deprecated, and rejected states. Link every shot to the exact approved asset or reference version used.

## Handoff

Provide scale, pivot/origin, orientation, units, color space, texture resolution, LOD expectations, collision, rig, naming, dependencies, and review images. Do not approve an asset solely from a beauty render; inspect it under production lighting and camera distance.

