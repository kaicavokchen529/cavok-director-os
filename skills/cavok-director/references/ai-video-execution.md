# AI Video Execution Supervisor

## 核心原则

AI视频Prompt不是把所有信息都塞进去，而是把最重要、最稳定、最有因果关系的变化写清楚。优先保证角色身份、空间、动作、摄影机和VFX状态连续。

## Prompt Priority

按以下优先级组织：

1. User Revision Scope / Approved Locks
2. Production Mode / Style Lock
3. Reference Responsibility Contract
4. Character Identity / Alias
5. Scene & Environment Lock
6. Blocking / Subject Motion / Physical State
7. Camera Movement & Lens
8. Lighting & Atmosphere
9. VFX Lifecycle
10. Sound / Dialogue Timing
11. Negative Constraints

## Revision Scope Lock

When the user has approved shots, states, or design decisions, treat them as frozen unless the user explicitly reopens them.

```text
APPROVED LOCK
Locked:
Editable:
Requested change:
Dependencies allowed to change:
```

“Only change Shot 05” means other approved shots remain unchanged. Do not improve unrelated composition, dialogue, blocking, VFX, wardrobe, geography, or timing while solving a local request. If the requested fix necessarily affects a dependency, state the dependency and change the minimum required layer.

## Character Alias

当角色已有参考图时，优先使用稳定别名，例如“佐一”“波二”“艾三”，并锁定对应参考图。首次出现写完整外观，后续只写发生变化的状态，避免每一镜重复长外貌导致注意力稀释。

## State Anchors

每个Part必须有：

- Start Frame：世界位置、身体体态、朝向、视线、左右手、支撑脚/重心、动量、接触关系、道具、伤势、VFX状态、光线、摄影机。
- End Frame：同样字段，作为下一Part唯一连续性基准。

角色位置、体态、左右手、服装、武器、伤势、接触关系和能力状态不得在Part边界无理由变化。

连续时空中执行 **Visible State Transition Law**：下一Part / 下一镜开头必须继承上一段结尾。若某个高风险状态容易被模型重置，只重复一条短的 **Continuity Risk Anchor**，不要复制整套设定。

## One Major Change Per Beat

复杂生成时，每个Beat优先只引入一个主要变化：发现、抬手、能力成型、发射、分离、结印、碰撞等。多个重大变化同时发生容易导致身份漂移、空间崩溃和动作丢失。

## Camera Separation

人物动作与摄影机动作分开写，但按真实因果顺序连接。不要机械规定Camera永远先写；如果人物先触发摄影机，应写“人物启动 → 摄影机晚半拍响应”。禁止把“角色向前冲，镜头也快速推近并环绕同时变焦”堆在同一句里。

## Shot Complexity Budget

复杂生成时，每个Beat / Shot默认控制在：

```text
1 Narrative Goal
1 Dominant Character Action
1 Primary Camera Idea
0–1 Secondary Camera Adjustment
1 Performance Change
1 Major FX / Environment Event
```

这是执行预算，不是机械配额。若多个重大动作、镜头技巧、表演转折和VFX事件互相竞争，优先拆Beat或利用稳定状态 / 动机遮挡分段，不继续堆Prompt。

## Prompt Budget

删掉不影响结果的形容词。重复信息只保留一次。优先保留可观察、可执行的名词和动词：位置、方向、距离、速度、光源、材质、接触和时间。

Reference Contract只写当前生成真正需要继承的职责。不要因为上传了一个参考，就让模型同时继承其中的人物、背景、姿态、构图和光线。

## Negative Constraint Compression

负面提示词优先覆盖最常见风险：身份变化、位置互换、提前动作、摄影机漂移、无来源光、廉价VFX、环境结构跳变。不要把几十条同义词堆成长墙。

## Retry Strategy

生成失败时不要整段重写。先判断失败类型：

- Identity Drift：缩短角色描述，强化别名/参考图。
- Blocking Collapse：减少同时动作，明确站位与触发顺序。
- Camera Drift：减少复合运镜并明确Settle。
- Cheap VFX：强化Source/Material/Lighting/Physics，减少“glow/energy”泛词。
- Environment Mutation：固定关键地标与光源方向。
- Prompt Overload：删除次要美术与重复形容词。

每次重试只修改最可能的根因。

## Timing

Part长度由目标模型能力、动作复杂度和连续性风险决定；模型支持更长时长不代表应该填满时长。对白必须给时间窗。复杂VFX要为Birth、Peak、Residual留出可读时间。不要在最后0.2秒同时完成多个状态变化。复杂段落优先在稳定状态、动机遮挡或明确动作落点处分段。

## QC

提交前检查：参考角色是否清楚？Start/End是否连续？主要变化是否太多？镜头和人物运动是否分开？VFX是否有生命周期？负面约束是否简洁且针对当前风险？