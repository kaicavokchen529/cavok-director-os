# AI Video Execution Supervisor

## 核心原则

AI视频Prompt不是把所有信息都塞进去，而是把最重要、最稳定、最有因果关系的变化写清楚。优先保证角色身份、空间、动作、摄影机和VFX状态连续。

## Prompt Priority

按以下优先级组织：

1. Production Mode / Style Lock
2. Character Identity / Alias
3. Scene & Environment Lock
4. Camera Movement & Lens
5. Blocking / Subject Motion
6. Lighting & Atmosphere
7. VFX Lifecycle
8. Sound / Dialogue Timing
9. Negative Constraints

## Character Alias

当角色已有参考图时，优先使用稳定别名，例如“佐一”“波二”“艾三”，并锁定对应参考图。首次出现写完整外观，后续只写发生变化的状态，避免每一镜重复长外貌导致注意力稀释。

## State Anchors

每个Part必须有：

- Start Frame：人物位置、姿态、视线、道具、伤势、VFX状态、光线、摄影机。
- End Frame：同样字段，作为下一Part唯一连续性基准。

角色位置、左右手、服装、武器、伤势和能力状态不得在Part边界无理由变化。

## One Major Change Per Beat

复杂生成时，每个Beat优先只引入一个主要变化：发现、抬手、能力成型、发射、分离、结印、碰撞等。多个重大变化同时发生容易导致身份漂移、空间崩溃和动作丢失。

## Camera Separation

人物动作与摄影机动作分开写。先写Camera，再写Subject。禁止把“角色向前冲，镜头也快速推近并环绕同时变焦”堆在同一句里。

## Prompt Budget

删掉不影响结果的形容词。重复信息只保留一次。优先保留可观察、可执行的名词和动词：位置、方向、距离、速度、光源、材质、接触和时间。

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

AI视频Part原则上≤15秒。对白必须给时间窗。复杂VFX要为Birth、Peak、Residual留出可读时间。不要在最后0.2秒同时完成多个状态变化。

## QC

提交前检查：参考角色是否清楚？Start/End是否连续？主要变化是否太多？镜头和人物运动是否分开？VFX是否有生命周期？负面约束是否简洁且针对当前风险？