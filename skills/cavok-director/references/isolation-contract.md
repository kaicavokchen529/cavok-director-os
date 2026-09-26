# CAVOK Skill Isolation Contract

## Purpose

Keep CAVOK Director OS complete, self-contained, and independent from unrelated Skills, legacy directing systems, hidden prompt layers, and previous assistant outputs.

## Rule-source boundary

The only normative rule sources for this Skill are:

1. the active user request and explicit user-approved project decisions;
2. `skills/cavok-director/SKILL.md`;
3. files referenced by that Skill inside `skills/cavok-director/`.

Installed Skills outside this directory are not normative inputs. They may be used only when the user explicitly requests a separate task, and their rules must not be merged into CAVOK.

## Conversation boundary

Previous conversation context may provide only explicit project facts, approved locks, reference responsibilities, revision scope, or continuity state that the user has confirmed or that is directly required by the current request.

Previous assistant suggestions, old prompts, remembered workflows, and unconfirmed interpretations are not CAVOK rules. Do not silently promote them into project truth.

When required information is missing, classify it as Unknown, Inference, or Director Proposal according to the evidence rules. Do not fill the gap with unrelated conversation context.

## Conflict handling

When an external Skill, historical instruction, reference, or conversation memory conflicts with this package:

- preserve the current user's explicit request;
- preserve approved CAVOK project locks;
- keep the conflict visible;
- do not merge the conflicting methodology;
- ask for clarification when the conflict changes the directing result.

Never silently combine two directing systems and present the result as pure CAVOK.

## Reference boundary

External images, videos, prompts, documents, and model adapters may provide evidence or execution constraints, but each must have an explicit responsibility. A reference may not silently become a source of CAVOK directing rules.

## Clean-room improvement protocol

External Skills and legacy systems may be audited for general design ideas only. Before a mechanism enters CAVOK:

1. describe the production problem in CAVOK terms;
2. verify that the mechanism does not already exist in this package;
3. extract the smallest general principle, not the source wording, characters, examples, fixed combinations, project facts, or universal numerical quotas;
4. rewrite the principle independently and assign one CAVOK authority file;
5. route it explicitly from `SKILL.md` and replace competing definitions with pointers;
6. add a regression case and run package validation.

An audited source never becomes a runtime dependency. CAVOK must remain executable when that source is absent.

## Completeness rule

Any rule required for CAVOK execution must live in this package or in a relative file explicitly routed by `SKILL.md`. Do not depend on hidden chat memory, another Skill, an unlisted local file, or an undocumented legacy system.

## Isolation QC

Before delivery, check:

- [ ] No unrelated Skill was used as a hidden rule source.
- [ ] No previous assistant output was treated as authoritative without user confirmation.
- [ ] No unconfirmed project inference was promoted to fact.
- [ ] Every loaded CAVOK reference belongs to this package.
- [ ] Any external model adapter changed execution syntax only, not directing logic.
- [ ] Any externally inspired mechanism was independently rewritten, assigned one authority, and regression-tested.
- [ ] The result can be reproduced from the current request, approved project state, and this package alone.
