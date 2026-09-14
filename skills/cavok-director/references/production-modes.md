# 视觉制作模式

## 选择矩阵

将风格拆为四层：媒介（真人/3D/2D/混合）、现实等级（写实/超写实/风格化/超现实）、类型、摄影策略。不要只写“国漫风”“某部动画风”或“真人风”。先决定媒介逻辑，再决定现实等级、动作语法和摄影方式。

## 3D Animation

允许强化 Pose、夸张动作、高速摄影机、残影、能量拖尾和设计化灯光，但保持动作、空间和视觉连续性。3D可以借用2D动画的Pose与Timing原则，但不要在未明确要求时自动加入手绘Smear、Impact Frame或背景抽象。

## Hyperreal Live Action

优先物理、表演、摄影、光线、材质和环境互动可信。真人表演默认克制；真实动作包含准备、重心转移、动作、惯性与恢复。摄影机必须说明 Tripod、Dolly、Steadicam、Handheld、Gimbal、Crane、Drone 等现实承载方式。允许轻微重新构图、跟焦迟滞和操作惯性，禁止随机抖动与幽灵摄影机。

## Stylized Live Action

以真实演员和真实摄影逻辑为基础，允许极端色彩、光影、构图和隐喻；基础人体物理仍需可信。除非明确切换到2D/混合动画语言，否则不要用手绘变形帧代替真实受力。

## 2D / Anime

2D动画不是“真人动作 + 卡通滤镜”。当动作设计以关键Pose、变量Timing、Smear、手绘FX、图形化Impact和背景抽象为主时，加载 [2d-anime-combat-grammar.md](2d-anime-combat-grammar.md)。

优先级：

```text
战术意图
→ 攻击方向
→ Key Pose
→ Silhouette
→ Timing / Spacing
→ Contact
→ Deformation
→ Consequence Pose
→ FX Drawing
→ Camera / Editing
```

允许：

- 夸张透视与强Foreshortening；
- variable timing、On Ones / On Twos感觉与held drawings；
- limb / weapon / body smear；
- 少量低细节afterimage；
- directional / radial / convergence / arc speed lines；
- hand-drawn impact FX、ink/brush/line effects；
- 根据强度降低背景细节或短暂进入graphic impact background；
- 关键冲击的高反差、反相、线稿、墨迹、剪影等Impact Frame。

必须保留：

- 攻击者与防御者关系；
- 攻击轴和银幕方向；
- 接触点；
- 战术状态变化；
- 角色身份与武器身份；
- 命中后的结果Pose和Recovery。

禁止把“速度线更多”“粒子更多”“摄影机更乱”当作高质量2D战斗。FX只能强化已经成立的Pose、方向与Timing。

当目标生成模型为Seedance 2.5时，先用2D动画战斗语法完成导演设计，再加载 `seedance-2.5.md` 转译成模型执行Prompt；模型适配器不得反过来改变战术因果、关键Pose、角色战斗签名和空间关系。

## Hybrid CG + Live Action

真人摄影逻辑为底，CG增强世界规模、角色能力、生物、环境和 VFX。CG必须匹配真实光线、材质、镜头与环境反应。

若混合项目明确使用2D动画插帧、手绘FX、Impact Frame或漫画式图形段落，应把这些段落视为独立媒介状态，并明确切入和退出点；不要让真人摄影规则与2D变形规则在同一帧互相冲突。
