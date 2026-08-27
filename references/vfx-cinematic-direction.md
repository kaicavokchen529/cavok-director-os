# Cinematic VFX Direction Module

## 核心原则

VFX不是装饰，而是摄影机记录的真实异常物理事件。
所有能力必须遵循：

来源 Source → 形成 Formation → 材质 Material → 光影 Lighting → 接触 Interaction → 余波 Secondary Effects → 消散 Dissipation

禁止只描述“出现一个特效”。必须描述“一个现象如何发生”。

---

## 1. Ability Source 能力来源

先定义能力来自哪里：

- 生理释放
- 能量转换
- 元素控制
- 空间变化
- 外部装置

来源必须影响表现形式。

错误：蓝色能量生成冰剑。

正确：空气湿度下降，水分冻结，晶体结构成长为冰刃。

---

## 2. Formation 形成过程

任何VFX必须有前兆。

冰：
- 空气折射变化
- 温度下降
- 呼吸白雾
- 水滴冻结
- 霜晶扩散
- 晶体结构成长

火：
- 空气热扰动
- 热浪折射
- 氧气流动变化
- 火焰层级形成

不要瞬间出现，不要无来源发光。

---

## 3. Material 材质逻辑

冰：
- 透明冰体
- 晶体结构
- 内部气泡
- 光线折射
- 冻结纹理

火：
- 燃烧层级
- 白热核心
- 不稳定火舌
- 热空气扭曲

雷：
- 电弧分叉
- 等离子路径
- 空气电离

特效必须像真实材料，不像游戏技能。

---

## 4. Lighting Interaction 光影互动

VFX必须影响环境：

冰：
- 蓝白反射进入人物和环境
- 叶片结霜
- 空气冷凝

火：
- 暖色反射人物脸部
- 树叶受热变化
- 周围产生热浪

光源必须有来源，禁止无理由轮廓光。

---

## 5. Physics Interaction 物理反馈

高级VFX必须有Secondary Effects：

冰：
- 碎冰
- 冷雾
- 水汽
- 温度变化

火：
- 火星
- 灰尘
- 空气膨胀
- 树叶运动

能力越强，环境反馈越重要。

---

## 6. Dissipation 消散

结束不是消失。

冰：
冻结 → 裂纹 → 碎裂 → 融化 → 水汽

火：
燃烧 → 减弱 → 火星 → 烟雾 → 熄灭

空间：
扭曲 → 恢复 → 残留影响

---

## 7. Hyper-Speed Character Light 超高速人物光影

适用于高速斩击、瞬移式近身、残像攻击和多方向连续突袭。

### 光谱层级

推荐色彩结构：

- 冷白 / 蓝白：最亮核心，应用于刀刃、动作前缘、瞬时爆闪。
- 青蓝 / Azure：主体高速能量与主要残影颜色。
- 电光蓝：光轨中段、人物运动边缘。
- 淡蓝紫：残像外围与衰减尾迹。
- 暖白金 / 少量橙黄：只用于真实命中火花和接触点，作为冷色能量的对比。

实用比例可参考：60% 冷白蓝 + 30% 青蓝 + 10% 蓝紫。此为导演级视觉近似，不是固定官方色值。

### 人物本体规则

- 人物不能整体变成持续蓝色发光体。
- 正常肤色、服装材质与环境曝光必须保留。
- 冷白/青蓝动态高光只出现在运动前缘、肩线、发梢、手臂和武器边缘。
- 面部只接受局部能量反射，不能被整张染蓝。

### 刀轨与残像

- 高速斩击光效必须附着于真实刀刃运动轨迹。
- 光轨中心靠近刀刃处最亮、最实，尾端快速降低透明度并碎裂衰减。
- 不同斩击轨迹长度和弧度应服从真实挥砍路径，禁止复制同一条月牙光效。
- 高速位移可形成1–2层低透明时间残像，残像沿运动方向拉伸，在约0.1–0.4秒内快速衰减。
- 残像是Temporal Echo，不是角色复制人。

### 命中光效

- 每次真实接触只产生一次极短命中爆闪。
- 同步出现方向一致的金属火星、碎屑、空气扰动或衣物受力。
- 禁止每一刀都产生巨大能量爆炸。

### 节奏规则

高速连续斩击应遵循：
锁定 → 爆发启动 → 消失 → 残像 → 异位重现 → 单次重击 → 再消失 → 多方向连续斩击 → 节奏压缩 → 短暂停顿 → 终结斩 → 余波。

---

## VFX Prompt Template

Source:
能力来源。

Formation:
生成过程和时间顺序。

Material:
材质、结构、透明度、纹理。

Lighting:
对人物、环境和摄影机的光影影响。

Physics:
碰撞、碎片、空气、环境反馈。

Dissipation:
消散过程。

---

## Negative VFX Constraints

禁止：
- anime energy aura
- game skill effect
- magic circle
- random particles
- instant appearance
- fake glowing material
- plastic crystal
- unrealistic explosion
- no environmental reaction
- no lighting interaction
- no physical lifecycle
- full-body blue glow
- identical neon slash trails
- giant crescent slash on every hit
- excessive particle spam
- lingering aura with no source

目标：高预算真人电影级VFX可信度，物理、材质、光线、空间和生命周期同时成立。
