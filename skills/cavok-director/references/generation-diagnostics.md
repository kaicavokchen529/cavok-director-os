# Generation Diagnostics

## Diagnose before rewriting

Preserve what works. Compare the result against the intended beat, then locate the first failing layer:

1. story information;
2. viewpoint and geography;
3. identity and continuity;
4. performance and blocking;
5. camera and focus;
6. action timing and physics;
7. material and VFX lifecycle;
8. lighting and compositing;
9. sound;
10. temporal artifacts and model limitations.

Fix the earliest causal failure plus dependent layers. Do not rewrite composition when only material response failed.

## Diagnostic record

```text
Expected observable result:
Observed result:
First incorrect frame or beat:
Preserved strengths:
Failure layer:
Likely cause:
Evidence:
Minimum correction:
Regenerate, extend, edit, composite, or accept:
Success criterion for next test:
```

## Common mappings

| Symptom | Likely layer | First correction |
|---|---|---|
| Characters separate too early | blocking/timing | bind separation to an explicit visible trigger |
| POV feels reversed | viewpoint | restate observer, detection beat, then observed subject |
| Camera floats continuously | camera | define start, travel, arrival, and hold |
| Ice looks blue and plastic | material | remove emission; add transparency, inclusions, reflection, refraction |
| Fire becomes an orange ball | formation | specify directed jet, turbulent expansion, hot core, unstable tongues |
| Collision becomes generic explosion | physics | describe contact, mutual change, force direction, residue |
| Face changes mid-shot | identity/temporal | shorten shot, strengthen reference, reduce simultaneous complexity |
| Light changes globally | lighting | constrain effect light locally and preserve ambient exposure |

## Retry ladder

Attempt the least expensive remedy:

1. use a better in/out point in editing;
2. adjust timing or prompt emphasis;
3. regenerate only the failing shot;
4. simplify simultaneous actions;
5. split the shot at a stable state;
6. generate separate passes and composite;
7. move the task to Unreal or another controllable pipeline.

Record model-specific errors separately from general directing rules.

