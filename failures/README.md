# CAVOK Failure Library

失败库优先记录可观察症状，而不是只保存失败Prompt。每条记录遵循：Symptom → Likely Cause → Diagnostic Questions → Fix → Preventive Rule → Verified Example。

## Failure Categories

- camera-drift.md：无目的漂移、机械推拉、停不住。
- character-identity-drift.md：脸、发型、服装、身高比例变化。
- blocking-collapse.md：人物站位、接触关系、左右位置或重心崩坏。
- action-weightless.md：动作无准备、无受力、滑步、漂浮。
- vfx-cheap-cgi.md：塑料材质、霓虹发光、游戏技能感。
- over-glow-particle-spam.md：Aura过强、粒子满屏、主体被吞没。
- environment-mutation.md：树木、建筑、天气、光源随机变化。
- continuity-break.md：跨Part状态、伤口、道具、左右手不连续。
- prompt-overload.md：描述过长导致模型忽略关键动作与空间。

## 使用规则

1. 先定位症状，不立刻重写全部Prompt。
2. 一次只修一个主因，便于验证。
3. 有效修正规则至少复现一次后才提升为正式Reference规则。
4. 失败记录优先保存“什么不要做”和“为什么失败”。
5. 项目结束时从失败库提取New Rule Candidate。