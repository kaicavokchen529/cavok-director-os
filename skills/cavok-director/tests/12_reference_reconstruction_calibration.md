# 12 Reference Reconstruction / Calibration

## Brief

The user supplies one still image of a character standing in a narrow corridor and one generated test frame that is intended to match it. The still clearly shows composition, subject occupancy, horizon, visible practical lights, wall spacing, foreground overlap, and the character's instantaneous pose. It does not show how the camera moved before or after the frame.

The generated frame matches face identity, wardrobe, and pose, but the corridor feels too wide, the subject appears too far from camera, and the background practicals are too bright.

## Requirements

Diagnose and revise using CAVOK evidence and calibration discipline.

Show:

- what is Observed from the still;
- what remains Inferred or Unknown;
- what new camera / lighting changes are Director Proposals;
- geometry-before-lens reasoning;
- MATCHED / DEVIATION / NOT EVALUABLE classification;
- a Matched Dimension Lock;
- one primary cause group to change;
- protected dimensions that must not regress;
- a measurable success criterion for the next test.

Do not claim camera motion, duration, or cut timing from the still.

## Critical Failures

- treating an inferred focal length as proven fact;
- claiming the still proves camera movement;
- changing face, wardrobe, or pose while fixing corridor geometry;
- fixing corridor width only with focal length while preserving wrong camera/subject/background distance;
- declaring visual validation without inspecting a new generated result.
