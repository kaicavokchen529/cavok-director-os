# Failure: Camera Drift

## Symptom

摄影机持续缓慢漂移、每镜都推近、人物停下后机位仍滑动、Pan/Tilt机械匀速、无理由Orbit或Zoom。

## Likely Causes

- Prompt只写“cinematic camera movement”，没有运动起止点。
- 没有Settle/Hold要求。
- 同一镜头塞入过多运动指令。
- 摄影机运动没有由人物动作或信息变化触发。

## Diagnostic Questions

- 摄影机为什么在这个时刻移动？
- 如果固定机位，信息是否仍成立？
- 是否写明Acceleration / Deceleration / Settle？
- 是否同时要求了Push、Pan、Orbit、Zoom等互相竞争的运动？

## Fix

- 写清 Start → Trigger → Move → Decelerate → Settle → Hold。
- 每个Beat只保留一个主要摄影机变化。
- 人物先触发摄影机，摄影机不要提前预测。
- 动作戏优先固定宽景让人物穿过构图。

## Preventive Rule

没有叙事理由时优先Static或轻微Reframe。高级感来自速度曲线和停点，不来自持续运动。