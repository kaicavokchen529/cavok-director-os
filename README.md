# CAVOK Director OS

面向 AI 影视创作的导演组 Skill：把故事、角色设定或粗略画面想法整理为可执行的电影级分镜、场面调度、动作设计、声音设计与视频生成提示词。

## 当前 Skill

`skills/cavok-director/`

- `SKILL.md`：核心工作流、强制规则与交付标准
- `references/director-framework.md`：故事、视角、调度、摄影、动作、灯光、声音与审核体系
- `references/cinematic-vfx.md`：电影级物理 VFX 导演模块
- `references/unreal-vfx-execution.md`：Chaos、Niagara、Lumen 与 Sequencer 的 Unreal 执行层
- `references/continuity-direction.md`：人物、动作、道具、灯光、伤势与 VFX 连续性
- `references/model-adapters.md`：不同 AI 视频模型的能力探测与提示词适配
- `references/generation-diagnostics.md`：生成结果故障分类、根因判断与最小修正
- `references/performance-direction.md`：表演、潜台词、微行为与人物关系调度
- `references/action-direction.md`：动作设计、战术节拍、能力配合与镜头覆盖
- `references/cavok-action-signature.md`：CAVOK 条件式快切动作语言与空间保护规则
- `references/action-prompt-engineering.md`：动作链路、速度、力量、运镜触发、人物比例与模型提示词压缩
- `references/camera-shot-decision-system.md`：根据内容选择景别、机位、焦段、运镜与镜头组
- `references/editing-direction.md`：剪辑结构、节奏、转场与失败素材抢救
- `references/sound-direction.md`：对白、环境、Foley、VFX 声音与混音透视
- `references/color-finishing.md`：曝光、调色、纹理与多段生成画面统一
- `references/art-assets.md`：角色、场景、道具、材质与参考资产管理
- `references/production-legal.md`：制片拆解、预算、审核、版权与发布安全
- `references/templates.md`：分镜表、生成提示词、VFX、连续性与迭代模板
- `agents/openai.yaml`：Codex UI 元数据

## 核心原则

镜头不是漂亮画面的堆叠，而是一系列具有明确视角、空间关系和因果顺序的可拍摄事件。

视觉特效也不是发光装饰。所有能力和异常现象都应具备：

> 来源 → 前兆 → 形成 → 传播 → 接触 → 反馈 → 余波 → 消散

## 使用示例

```text
Use $cavok-director to 把下面的剧情整理成 15 秒真人电影质感分镜，并输出可直接用于视频生成模型的完整提示词。
```

也可以用于诊断已有生成结果：

```text
Use $cavok-director to 保留现有镜头构图，只诊断并修正冰火碰撞的材质、光影与物理反馈。
```

## 安装

将 `skills/cavok-director` 目录放入 Codex 的 Skills 目录，或在支持仓库 Skill 的环境中直接引用该目录。

## 适用范围

- 真人电影与真人漫改
- 动画与国漫 3D
- 游戏 CG 与剧情预演
- AI 视频分镜和提示词
- 生成结果的导演复盘与规则沉淀
