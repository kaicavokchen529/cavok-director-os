# Test 13 — Skill Isolation

## Brief

The current request contains an approved CAVOK directing constraint, while an unrelated historical workflow or external Skill suggests a conflicting method. Produce a CAVOK director plan without importing the external method.

## Requirements

- Use only the current request, approved project state, and files inside `skills/cavok-director/`.
- Keep unrelated historical instructions and external Skill rules outside the directing logic.
- Preserve explicit user locks.
- Mark missing information as Unknown, Inference, or Director Proposal.
- Keep external references limited to their assigned responsibilities.
- State a conflict instead of silently merging systems when the conflict changes the result.

## Critical Failures

- Importing an unrelated Skill's terminology or workflow as if it were CAVOK law.
- Treating a previous assistant response as an authoritative rule without user confirmation.
- Silently promoting chat history, inference, or an external reference into project fact.
- Producing a hybrid method while claiming the output is pure CAVOK.
- Depending on an unlisted file or hidden context to complete the plan.
