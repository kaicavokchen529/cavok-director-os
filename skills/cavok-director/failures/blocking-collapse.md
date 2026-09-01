# Failure: Blocking Collapse

## Symptom

人物左右位置互换、搭肩/搀扶/对峙关系消失、角色提前分开、脚底滑步、重心不合理、人物与道具或树枝穿插。

## Likely Causes

- 没有锁定空间拓扑和人物接触关系。
- 只描述人物动作，没有描述彼此相对位置。
- 镜头切换后未继承上一镜End Frame。
- 同一Beat安排过多人物状态变化。

## Fix

- 明确A在左/B在右、谁前谁后、距离、朝向、接触点和支撑点。
- 接触关系写成硬状态：手肘搭肩、手掌不抓握、主重量由自己支撑。
- 每Part End Frame直接作为下一Part Start Frame。
- One Major Change Per Beat：一次只改变一个主要关系。

## Preventive Rule

Blocking必须以空间几何描述，而不是只写“靠在一起”“站在旁边”。