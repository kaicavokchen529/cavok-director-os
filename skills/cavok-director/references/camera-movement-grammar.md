# Camera Movement Grammar

> **职责边界：**本文件负责已经选定运镜的路径、速度曲线、承载质感、人物—摄影机相位关系与落幅执行。先由 [cinematography-language-engine.md](cinematography-language-engine.md) 决定视点制度、景别曲线、摄影平台、光学策略和表达型候选；本文件不得把情绪关键词自动映射成固定运镜。

## 核心原则

高级运镜不是“镜头一直动”，而是摄影机知道什么时候开始、为什么移动、何时减速、何时停住。每次运动都必须服务信息、Blocking、情绪、人物表演、动作向量或空间关系。

在真人 / 超写实CG动作中，摄影机不能成为独立的“炫技层”。加载 [hyperreal-action-direction-v2.md](hyperreal-action-direction-v2.md)，把人物表演、动作编排和摄影机编舞作为同一个事件设计。

核心动作摄影原则：

> **镜头不装饰动作；镜头从表演中获得张力，被动作触发，并随动作结果完成自己的运动。**

## Motion Curve

任何运镜优先写成：

Start → Trigger / Motivation → Acceleration → Cruise / Follow / Yield → Deceleration → Settle → Hold

禁止机械匀速移动到结束。真人摄影要保留承载方式带来的轻微惯性和重新构图，但不得随机漂移。

对于动作镜头，再增加人物与摄影机之间的相位关系：

- Character leads, camera follows；
- Character and camera launch together；
- Camera yields before subject arrival；
- Character moves while camera holds；
- Character and camera move in opposing vectors。

不要默认锁步同步。

## 基础语法

- Dolly In：压缩心理距离、确认、逼近、进入角色判断。动作场面中必须有认知、关系或不可逆决定作为触发；禁止把“战斗开始”本身当成急推理由。
- Dolly Out：释放、疏离、揭示环境或关系变化；也可用于命中后扩大可见位移。
- Pan：跟随注意力或重新分配画面信息。动作中可用于角色先动、镜头后追的reacquisition。
- Tilt：高低信息揭示、视线追踪、尺度建立。垂直动作中必须与跳跃、坠落、俯冲、台阶或高差有关。
- Truck：产生前后景视差，强化空间和关系。动作中可与纵深穿场结合，而不只做横向跟拍。
- Pedestal/Crane：改变权力高度、揭示空间或形成垂直转场；动作中由真实高低变化触发。
- Arc/Orbit：仅在需要读清前后站位、关系重组、绕开攻击轴或完成可见越轴时使用。禁止把orbit当“高级感”。
- Handheld：用于身体临场、危险、主观压力，幅度受控。
- Steadicam/Gimbal：连续调度与人物空间关系。

## 组合语法

- Dolly In + Pan：主体移动中进行注意力锁定。
- Truck + Dolly：制造强视差并改变心理距离。
- Arc + Push：展开双人关系后逐渐聚焦。
- Foreground Wipe + Rack Focus：用前景完成自然转场与信息接力。
- Tilt + Settle：从线索找到主体后停住读取。
- Push-to-Stop：摄影机跟随人物动作同时停止，形成重音。
- Pull-back Reveal：从细节拉回整体，揭示关系或后果。
- POV Reorientation：先建立身体位置，再用头部/视线运动寻找目标。

动作专用组合：

- Weapon Pass Transition：武器近镜掠过形成遮挡，用于换位、换轴、换焦段或隐藏剪辑；武器必须真实经过该空间。
- Body Pass Reframe：角色贴近镜头穿过后，摄影机再pan/rotate抓住下一攻击关系。
- Ground-Skim Launch：贴地机位由脚步、落地或蹬地动作触发，随后前冲或抬升。
- Axial Crash-In：攻击者沿镜头轴从远到近，摄影机后撤但慢于角色，制造快速尺度增长。
- Vertical Rise / Dive：镜头高度随真实跃起、俯冲、坠落、台阶或高差变化。
- Reverse Pull：命中或击飞后摄影机向反方向拉开，迅速放大位移结果。
- Motivated Axis Crossing：角色、前景或清晰弧线带摄影机跨轴；观众必须能看到换轴过程。
- Vector Match Cut：跨切镜保持上一镜的力量方向。
- Shot-inside-Shot：同一镜头允许从近景判断演化到追拍、近镜掠过、双人构图和接触稳定。

## Camera Breathing

优先使用：

Move → Settle → Discover → Hold → React → Move

动作场面更常用：

Hold → Character Tell → Character Launch → Camera Response → Spatial Expansion → Contact Stability → Consequence Movement → Settle

环境本身可以运动：树叶、光斑、云、发丝、衣摆、尘埃。摄影机不必为了“电影感”持续漂移。

## Tilt / Pan 的高级节奏

寻找目标时：启动慢 → 中段自然加速 → 接近目标减速 → 找到目标 → Hard/Soft Settle → Hold 0.5–1秒。

跟随人物时：尽量让人物先触发摄影机，而不是摄影机提前猜动作。高速动作中，摄影机可以短暂失去最优构图再重新捕捉，只要方向和地理仍然清楚。

## Dolly Zoom

仅用于空间感或心理空间真正发生变化时。幅度克制，主体大小保持相对稳定，背景透视缓慢改变。禁止把它当“高级感”装饰。

## Action Camera

动作戏首先保证银幕方向、攻击线路和因果可读，但“清楚”不等于始终站在侧面拍完整全身。

必须主动使用三维空间：

- X轴左右；
- Y轴前后纵深；
- Z轴高低；
- Camera Vector相对攻击线的方向。

除非故意采用横版视觉策略，连续两个主要攻击Beat不得都以纯横向侧视完成。

高速动作可以让摄影机固定，让动作穿过构图；也可以让角色先动、摄影机慢半拍追；关键接触前摄影机常应减速或稳定，让观众读清Contact与Force Transfer。

不要默认“打中 = 震镜”。冲击可以用完全稳定、延迟短促位移、主体主观后退、前景扰动、反向拉远等不同方式表达。

动作镜头需要区分职能：Geography / Performance / Threat / Mechanics / Immersion / Impact / Consequence / Reorientation。不要让每一镜都是Mechanics Shot。

## Camera Showmanship

真人 / 超写实CG动作允许炫技，但必须有因果。

Camera Flair分级：

- Flair 0：纯功能；
- Flair 1：轻度设计；
- Flair 2：明确动作摄影技巧；
- Flair 3：Hero Camera Move。

不设通用数量配额。根据场景长度、媒介、动作复杂度和戏剧重心建立主次层级：没有适合的Hero Camera Move可以不用；存在一个真正承重的摄影事件时，其他镜头应为它保留可读性和对比。不要每镜都做stunt camera，也不要为了“克制”而自动删除表达型候选。

任何明显炫技都必须回答：

1. 谁或什么触发摄影机？
2. 摄影机跟随的是哪一股力或哪一个信息变化？
3. 什么时候减速或停止？
4. 停止后让观众看见什么？

答不出来就删掉。

## Character Camera Signature

不同角色应有不同的动作摄影语言。

例如：

- 冷静高手：长Hold、人物先动、镜头稍后反应、Contact极稳；
- 狂暴角色：镜头让位、轴向压迫、前景被破坏、结果空间大幅改变；
- 高速角色：Body Pass、遮挡换位、Whip Reacquisition、纵深穿场；
- 优雅角色：平滑弧线、精确Reframe、透视接力、最少无意义震动。

摄影机也要说明“这个人怎么打”。

## Physical Support

真人模式必须说明现实承载：Tripod、Dolly、Slider、Steadicam、Handheld、Gimbal、Crane/Jib、Drone、Vehicle Rig、Body Rig。无法真实执行的“幽灵机位”仅在明确风格化CG模式下允许；即使是CG虚拟摄影，也应保持明确的动机、惯性和空间逻辑。

## Prompt Contract

英文摄影提示词以 Camera Movement 开头，并写明：Support + Angle + Lens + Start Position + Character Trigger + Lead/Lag Relationship + Direction + Speed Curve + Framing Evolution + Contact Behavior + Settle/Hold + Director Intent。

动作Prompt必须分开写人物运动与摄影机运动，但保持因果连接。

## Negative

禁止随机漂移、无理由Zoom、机械匀速推拉摇移、持续Orbit、无动机360度、频繁Whip Pan、无来源震镜、摄影机穿越实体、每镜都推近、没有停点、摄影机提前替人物释放张力、连续侧面中全景把战斗拍成横版格斗、人物和摄影机每次都锁步同步。
