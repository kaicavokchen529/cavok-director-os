# CAVOK Director OS

面向 AI 影视创作的导演组 Skill：把故事、角色设定、参考图或粗略画面想法整理为可执行的电影级导演方案、分镜、场面调度、动作/VFX设计、声音设计与视频生成提示词。

## 唯一正式 Skill

本仓库唯一 Source of Truth：

`skills/cavok-director/`

安装、引用、迭代和版本维护均以该目录为准。仓库根目录不再维护第二套 SKILL / references / failures / templates。

正式包包括：

- `SKILL.md`：总导演工作流、路由、强制规则与交付标准
- `references/`：导演、摄影、表演、动作、VFX、灯光、空气、声音、剪辑、调色、连续性、AI模型适配、Unreal、制片等专业模块
- `failures/`：生成失败症状、根因与最小修正库
- `templates/`：Project / Character / Scene / Continuity / Director Review 持久项目模板
- `agents/openai.yaml`：Skill UI 元数据

## 核心导演逻辑

> 剧情意图 → Scene Objective → Drama Beat → 人物目标 → 表演 → Blocking → 信息控制 → 构图 → Camera → Action → VFX → Lighting / Atmosphere → Sound → Editing → AI Execution → Continuity → Director QC

VFX按真实事件设计：

> Source → Precursor → Formation → Material → Propagation → Contact → Physical Feedback → Aftermath → Dissipation

强冲击进一步加入：

> Anticipation → Time Compression / Expansion → Contact → Impact Frame → Compression → Deformation → Energy Release → Secondary Reaction → Inertia → Recovery → Residual

## 使用

```text
Use $cavok-director to 把下面的剧情整理成真人电影级导演方案与可执行AI视频提示词。
```

也可以用于只修某一层：

```text
Use $cavok-director to 保留现有构图与表演，只诊断并修正这次冰火碰撞的VFX材质、冲击节奏与环境反馈。
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
- 生成结果导演复盘、Failure Library 与规则沉淀
