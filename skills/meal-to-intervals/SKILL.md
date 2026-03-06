---
name: meal-to-intervals
description: 参考 intervals 既有技能实现：当用户提供饮食照片或文字餐单时，估算单餐热量与三大营养素，并按 Intervals.icu API 规范写入（默认写入日历 NOTE 事件，可选更新 wellness 字段）。用于“记录这顿饭到 intervals.icu”“根据照片计算热量并同步”场景。
---

# Meal to Intervals

## Overview

按你现有 intervals 技能风格实现：
- 认证方式：`Basic Auth`（用户名固定 `API_KEY`，密码是你的 API key）
- 基础地址：`https://intervals.icu/api/v1`
- 运动员：从 `config.json` 读取 `athlete_id`

默认把每顿饭写成 Intervals 日历上的 `NOTE` 事件，备注里包含总热量和宏量营养；并且会**同步追加更新当日 wellness 健康字段**。同时支持 `wellness_only` 模式只写健康数据。

## 配置

在技能目录放一个 `config.json`（格式同 `assets/config_template.json`）：

```json
{
  "intervals_icu": {
    "api_key": "YOUR_INTERVALS_ICU_API_KEY",
    "athlete_id": "i123456"
  }
}
```

## 输入格式

见 `references/schema.md`。

## 用法

### 1) dry-run（先看计算结果）

```bash
python3 scripts/meal_to_intervals.py \
  --input /path/to/meal.json \
  --mode event_note \
  --dry-run
```

### 2) 写入 Intervals NOTE

```bash
python3 scripts/meal_to_intervals.py \
  --input /path/to/meal.json \
  --mode event_note
```

### 3) 可选：同时更新 wellness（支持体重/静息心率/HRV/睡眠/步数 + 营养汇总）

```bash
python3 scripts/meal_to_intervals.py \
  --input /path/to/meal.json \
  --mode event_note \
  --update-wellness
```

### 4) 只写健康数据（不写饮食事件）

```bash
python3 scripts/meal_to_intervals.py \
  --input /path/to/wellness.json \
  --mode wellness_only
```

## Workflow

1. 接收照片或文字餐单并整理成结构化 JSON。
2. 用 OpenFoodFacts 按食物名检索每 100g 营养并换算。
3. 汇总总热量/蛋白/脂肪/碳水。
4. 写入 Intervals 事件（NOTE）。
5. 可选更新 wellness。

## Notes

- 照片识别属于前置步骤：先识别食物与克重，再调用脚本。
- Intervals 官方没有稳定“饮食专用端点”，用 NOTE 事件是最稳落地方案。
- 如果你后续有私有饮食端点，再把脚本 mode 扩展为 `custom_endpoint` 即可。
