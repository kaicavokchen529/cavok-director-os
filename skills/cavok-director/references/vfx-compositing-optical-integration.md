# VFX Compositing & Optical Integration

## Goal

A physically designed effect can still look pasted-on if it does not share the photographed plate's optics, depth, exposure, atmosphere, motion and texture. Integration means the VFX appears to have passed through the same lens and recording pipeline as the live image.

## Integration stack

Plate Analysis → Depth/Occlusion → Light/Shadow → Reflection/Refraction → Motion → Lens Response → Atmosphere → Texture/Grain → Temporal Stability → Final Grade

## Plate analysis

Before compositing, record camera motion, lens class, focus distance, depth of field, shutter/motion blur, exposure, white balance, highlight clipping, grain/noise, lens distortion, flare, atmospheric density and moving occluders.

## Depth and occlusion

Effects must sit at a defined depth. Respect foreground occlusion, body parts crossing the effect, vegetation, architecture and volumetric media. Add contact shadow or local darkening where matter blocks light. A transparent effect still needs correct depth ordering.

## Light integration

Separate visible emission from scene illumination. Add local interactive light to skin, eyes, cloth, ground, walls, smoke and reflective materials according to distance and angle. Preserve original ambient/key direction. Use light wrap only where bright background light physically scatters around an edge; do not use it as a universal glow halo.

## Reflection and refraction

Reflect effects only on surfaces that can reflect them and with appropriate roughness. Refraction must distort the correct background layer and move consistently with camera parallax. Ice, glass, heat haze and portals require different optical behavior.

## Motion integration

Match shutter character and motion blur. Fast CG elements should not be razor sharp inside a blurred plate, nor excessively smeared when the live plate is crisp. Match camera shake and rolling/scan behavior only if present. Use motion vectors carefully around transparency and high-frequency edges.

## Focus and bokeh

CG depth must follow the plate focus plane. Defocus size and bokeh character should match the lens; foreground particles closer than focus may become soft, while contact effects at the subject plane remain readable. Do not blur the entire effect uniformly.

## Lens response

Match distortion, vignetting, chromatic behavior, flare/ghosting, halation and highlight roll-off only to the degree visible in the plate. Apply lens distortion after compositing so CG and plate share the same geometry. Avoid decorative chromatic aberration.

## Atmosphere

Place effects inside the same air. Distant effects lose contrast and saturation; bright effects illuminate nearby haze; smoke/steam partially occlude what lies behind them. Backlit particles and volume respond to the real light direction.

## Edge integration

Avoid perfectly clean CG mattes. Preserve natural motion blur, defocus, fine hair/foliage occlusion and semi-transparent edges. Edge contamination should come from actual neighboring light/color, not a generic colored fringe.

## Texture and grain

Match denoise, sharpness, grain scale, compression and local contrast after integration. Grain belongs over the final composite, but some volumetric/noisy effects may need internal texture before final grain. Do not sharpen CG independently until it looks cleaner than the plate.

## HDR and emission

Bright cores may approach or exceed display white, but maintain a small high-intensity area and natural roll-off. Bloom/halation is an optical response to brightness, not a substitute for emission structure. Keep daylight VFX readable through material, silhouette, distortion and local interaction rather than global bloom.

## Temporal stability

Audit edge chatter, matte boiling, particle popping, changing distortion, reflection flicker, inconsistent motion blur, exposure pumping and grain swimming across frames. Temporal consistency is more important than single-frame perfection.

## Contact checklist

- Does the effect touch the correct surface/body point?
- Is there contact shadow, reflection, heat/frost/wetness or deformation where appropriate?
- Does force direction match debris, cloth and body response?
- Does interaction continue for a few frames after primary contact?

## Prompt / review language

Use: `optically integrated into the photographed plate; matched depth, occlusion, shutter blur, focus plane, lens distortion, local interactive light, reflection/refraction, atmosphere, grain and temporal response`.

## Negative

No pasted-on glow, no uniform blur, no clean cutout edges, no impossible foreground ordering, no unmatched sharpness, no global color spill from a small source, no fake light-wrap halo, no decorative chromatic aberration, no temporally flickering composite.