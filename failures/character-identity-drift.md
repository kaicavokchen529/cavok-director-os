# Failure: Character Identity Drift

## Symptom

跨镜头或跨Part出现脸型变化、年龄变化、发型长度变化、发色变化、服装纹理变化、饰品丢失、身高比例漂移。

## Likely Causes

- 每一段重复重写角色描述，导致模型重新解释人物。
- 角色Reference没有Alias与固定状态锚点。
- Prompt中角色外观与动作描述混杂过多。
- 光线、焦段或妆造变化过剧烈，模型误判为新角色。

## Fix

- 建立Character Alias，例如：佐一 = Reference 01。
- 外观只在角色卡中完整定义，执行段主要描述动作与状态变化。
- 每个Part使用Start/End Frame锁定发型、服装、伤口、饰品、左右手和身高比例。
- 角色外观变化必须是剧情事件，而不是生成噪声。

## Preventive Rule

角色身份信息属于稳定层；动作、表情、受伤和光照属于变化层。不要在每一镜重新发明人物。