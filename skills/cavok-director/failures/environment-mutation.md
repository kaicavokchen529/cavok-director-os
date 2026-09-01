# Failure: Environment Mutation

## Symptom

树木、门窗、建筑、天气、云层、太阳方向、地面材质或道具位置跨镜随机变化。

## Cause

环境被当成背景形容词而不是连续性对象；缺少Environment Lock与Start/End Frame。

## Fix

锁定空间结构、主要树/门/窗/道路、光源方向、天气、时间、风向、破坏状态和关键道具位置。新Part继承上一Part End Frame。

## Rule

环境也是角色。只有剧情事件可以改变结构、天气、光源和破坏状态。