# CAVOK Director OS

面向 AI 影视创作的导演组 Skill：把故事、角色设定、参考图或粗略画面想法整理为可执行的电影级导演方案、分镜、场面调度、动作/VFX设计、声音设计与视频生成提示词。

## 唯一正式 Skill

本仓库唯一 Source of Truth：

`skills/cavok-director/`

安装、引用、迭代和版本维护均以该目录为准。仓库根目录不再维护第二套 SKILL / references / failures / templates。

正式包包括：

- `SKILL.md`：总导演工作流、路由、强制规则与交付标准
- `references/`：导演、摄影、光学、表演、动作、VFX、合成、灯光、空气、声音、剪辑、调色、连续性、AI模型适配、Unreal、制片、Spatial Previs、Evidence Discipline 与 Calibration 等专业模块
- `scene-grammars/`：角色登场、Boss Reveal、对峙、悬疑发现、追逐、决斗、超能力战、超高速突袭、元素碰撞、余波等场景语法
- `failures/`：生成失败症状、根因与最小修正库
- `templates/`：Project / Character / Scene / Continuity / Director Review 持久项目模板
- `scripts/`：包结构、内部引用、隔离标记与重复内容的确定性校验
- `tests/`：19 项固定导演回归测试与评分卡，包含 Spatial Previs、Reference Reconstruction / Calibration、Skill Isolation、Adaptive Duel、Cinematography Language、Movement/Angle/Temporal Grammar、Action–VFX–Camera Orchestration 与 Package Integrity 专项测试
- `agents/openai.yaml`：Skill UI 元数据

## 核心导演逻辑

> 剧情意图 → Scene Objective → Drama Beat → Scene Grammar → 人物目标 → 表演 → Blocking → 信息控制 → 构图 → Camera → Optics → Action → VFX → Compositing → Lighting / Atmosphere → Sound → Editing → AI Execution → Continuity → Director QC

VFX按真实事件设计：

> Source → Precursor → Formation → Material → Propagation → Contact → Physical Feedback → Aftermath → Dissipation

强冲击进一步加入：

> Anticipation → Time Compression / Expansion → Contact → Impact Frame → Compression → Deformation → Energy Release → Secondary Reaction → Inertia → Recovery → Residual

## 当前关键能力

- Scene Grammar Library：让系统知道“这类戏如何发展”，而不是只知道“镜头怎么拍”。
- Cinematography Language Engine：以视点、景别、位置/角度、摄影平台、光学、运动拓扑、时间行为七个维度统一选镜；让第一人称、俯拍/顶拍、荷兰角、急推/后拉、变焦、子弹时间、速度渐变、Steadicam、手持、无人机、FPV穿越机与虚拟摄影机在适合时主动进入候选。
- Action–VFX–Camera Orchestration：把合法动作、动作阶段、力量向量、VFX功能、摄影机关系、镜头职能、景别、时间处理、接触和后果组合成候选方案；明确拳脚、擒拿、投技、刀剑、跳跃、高速位移、投射物、能量束、碰撞、瞬移与变身的适配边界，但不建立固定配方。
- Combat Decision Engine：通过能力边界、战术状态、合法动作选择、证据驱动的对手适应、主动权转移和动作价值门，防止固定连招、无意义动作与沙袋式对手。
- Hyperreal Action Direction v2：把人物表演、三维动作调度和摄影机编舞耦合，避免横板格斗、装饰性运镜和机械跟拍。
- 2D Anime Combat Grammar：独立处理 Key Pose、Silhouette、Variable Timing、Smear、Impact Frame、手绘FX和背景抽象。
- VFX Compositing & Optical Integration：统一深度、遮挡、互动光、反射折射、运动模糊、焦点、镜头响应、空气与颗粒质感。
- Camera Optics & Sensor：补齐传感器、焦距/距离、T-stop、焦点、呼吸效应、球面/变形宽银幕、快门、滚动快门、高光、滤镜与眩光，并执行 Geometry Before Lens。
- Production / Previs / Evidence Gates：加入 Fact / Observation / Inference / Director Proposal / Unknown、R0/R1/R2 Readiness、Spatial Previs、Light Source Causality、Dominant Depth、Volumetric Double Gate、Evidence Boundary 与 Matched Dimension Calibration。
- Execution Discipline：加入 Approved Lock、Reference Responsibility Contract、Physical State Ledger、Visible State Transition Law、Continuity Risk Anchor、Sound Continuity 与 Shot Complexity Budget。
- Director Mechanism Library：导演经验按 Activation → Dramatic Problem → Mechanism → Visible Result → Exit → Anti-Trigger 组织，避免只学表面风格标签。
- Rule Authority Map：同一概念只保留一个规范定义，其他模块仅路由或执行，避免规则复述和版本漂移。
- Director Regression Tests：当前扩展到 19 项，并加入战术适应、摄影语言、运动/角度/时间语法、动作–VFX–摄影编排、Skill 隔离和包完整性验证。

## 使用

```text
Use $cavok-director to 把下面的剧情整理成真人电影级导演方案与可执行AI视频提示词。
```

也可以用于只修某一层：

```text
Use $cavok-director to 保留现有构图与表演，只诊断并修正这次冰火碰撞的VFX材质、冲击节奏、光学合成与环境反馈。
```

## 安装

将 `skills/cavok-director` 目录放入支持 Skills 的环境中，或直接引用该目录。

## 适用范围

- 真人电影与真人漫改
- 动画与 3D CG
- 游戏剧情 CG / Unreal Cinematic
- AI 视频分镜与生成提示词
- 动作与超能力 VFX
- 多段生成连续性管理
- 光学/合成真实性审核
- 生成结果导演复盘、Failure Library 与规则沉淀
- Skill 版本回归测试与质量验证

## Isolation and independence

CAVOK Director OS is a self-contained Skill package. Its normative rules come only from the active user request, approved project decisions, `skills/cavok-director/SKILL.md`, and files routed inside that directory.

Unrelated Skills, legacy workflows, hidden prompt layers, and unconfirmed historical conversation outputs must not be merged into CAVOK. External references and model adapters may affect evidence or execution syntax only when their responsibilities are explicit. General ideas learned from an external system must be independently rewritten, assigned one CAVOK authority, regression-tested, and remain executable without the source. See [isolation-contract.md](skills/cavok-director/references/isolation-contract.md), [Test 13](skills/cavok-director/tests/13_skill-isolation.md), and [Test 15](skills/cavok-director/tests/15_package-integrity.md).
