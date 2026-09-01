# Failure: Prompt Overload

## Symptom

模型忽略关键动作、角色关系变差、运镜执行混乱、VFX与环境互相污染，提示词越写越长但结果更不稳定。

## Cause

同一Part塞入过多主要变化；角色稳定信息与临时动作重复；形容词堆叠；摄影、人物、环境、VFX指令互相竞争。

## Fix

- One Major Change Per Beat。
- 稳定信息进入Character/Environment Bible，不在每镜重复。
- 每镜优先顺序：主体动作 > 空间关系 > Camera > 光线 > VFX >细节。
- Negative只保留高风险错误。
- 复杂动作拆Part或拆Beat，不用形容词解决时序问题。

## Rule

Prompt不是文学描述，而是执行预算。每一个词都应帮助模型确定身份、空间、动作、时间或视觉结果。