# Failure: Cheap CGI VFX

## Symptom

特效像游戏技能、塑料水晶、霓虹光带、统一发光球；没有材质、环境反应、接触反馈或消散过程。

## Likely Causes

- 只用颜色和“energy/glow”描述VFX。
- 没有定义真实材料和光学响应。
- 没有Source、Formation、Contact、Secondary Effects。
- Emission过强，吞掉主体材质和正常曝光。

## Fix

- 使用Source → Formation → Material → Lighting → Interaction → Secondary Effects → Dissipation。
- 描述透明度、裂纹、气泡、折射、烟、蒸汽、热扰动、碎屑等真实物理特征。
- 发光只作为局部结果，不作为材质本体。
- 必须让皮肤、衣物、地面、空气和环境对VFX产生响应。

## Preventive Rule

禁止只写“蓝色冰能量”“橙色火球”“强烈魔法光效”。优先描述摄影机能记录到的异常物理现象。