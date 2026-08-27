# Failure: Continuity Break

## Symptom

跨镜伤口、血迹、武器、左右手、道具状态、人物站位、视线方向和VFX状态不连续。

## Cause

只保存角色身份，没有保存状态；Part之间缺少End/Start Frame锚点。

## Fix

为每个镜头和Part记录：人物位置、朝向、手部状态、服装、伤口、道具、环境破坏、VFX阶段、光源方向。上一Part End Frame直接成为下一Part Start Frame基准。

## Rule

Continuity是状态机，不是描述风格。任何状态变化必须有画面中的原因。