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

Label each reference as identity, costume, pose, lighting, environment, lens, material, VFX, or mood. Do not let a mood reference silently override identity or geography. Record source, license, date, and allowed usage.

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

