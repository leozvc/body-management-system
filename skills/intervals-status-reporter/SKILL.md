---
name: intervals-status-reporter
description: 基于 intervals.icu 的身体状态分析技能。获取健康指标（HRV/睡眠/心率）、训练负荷（CTL/ATL/TSB）、运动记录，生成身体状态报告与训练建议。
---

# intervals-status-reporter - 身体状态分析技能

此技能基于 intervals.icu 数据平台，提供个人身体状态分析与训练决策支持。

## 功能

- **健康指标查询**: 获取 HRV、静息心率、睡眠时长与质量、体重等数据
- **训练负荷分析**: 计算 CTL（体能）、ATL（疲劳）、TSB（状态）指数
- **运动记录同步**: 读取近期运动类型、时长、热量、心率区间
- **状态报告生成**: 一键生成标准化身体状态报告（`body_status_report.py`）
- **训练决策支持**: 基于 TSB 疲劳指数推荐/避免的训练强度

## 如何使用

### 1. 配置 Intervals.icu 凭证

在使用本技能之前，您需要提供 intervals.icu 的 API 密钥和您的运动员 ID。请在技能的 `assets/config_template.json` 文件中填写这些信息，并将其保存为 `config.json`。

**`config.json` 示例:**

```json
{
  "intervals_icu": {
    "api_key": "YOUR_INTERVALS_ICU_API_KEY",
    "athlete_id": "i206099"
  },
  "fitness_goals": {
    "primary_goal": "weight_loss",
    "training_days_per_week": 5
  }
}
```

### 2. 获取身体状态报告（标准化输出）

使用 `scripts/body_status_report.py` 脚本生成标准化身体状态报告。

示例：
```bash
python scripts/body_status_report.py
```

输出包含：核心指标、训练负荷、近期运动、今日摄入、训练建议、恢复建议

### 3. 获取原始数据（高级用户）

使用 `scripts/intervals_api.py` 脚本来获取原始 JSON 数据。

示例：
```bash
python scripts/intervals_api.py --action get_summary_data
```

### 4. 生成训练计划

使用 `scripts/fitness_planner.py` 脚本来根据当前状态生成训练计划。

示例：
```bash
python scripts/fitness_planner.py --action generate_plan --goal weight_loss
```

### 5. 查看参考资料

- **`references/intervals_api_docs.md`**: intervals.icu API 详细文档
- **`references/fitness_principles.md`**: 科学训练原则与方法

## 触发场景

- "查看我今天的身体状态"
- "我今天适合训练吗"
- "生成今日健康报告"
- "最近训练负荷怎么样"
- "我恢复好了吗"

## 输出示例

```
📊 身体状态报告
**日期**: 2026-03-06 14:55

═══ 核心指标 ═══

✅ **静息心率**: 56 bpm
✅ **HRV**: 62.0 ms
❌ **睡眠**: 5h 48m (评分：71.0)

═══ 训练负荷 ═══

**CTL** (体能): 18.0
**ATL** (疲劳): 25.3
**TSB** (状态): -7.3 - 🟡 轻度疲劳

═══ 训练建议 ═══

✅ **推荐**: Zone 1-2 低强度训练、技术练习
⚠️ **避免**: 高强度间歇、长时间耐力训练

═══ 恢复建议 ═══

😴 **优先补觉** - 昨晚睡眠不足，今晚目标 8h
```

## 资源

- **`scripts/body_status_report.py`**: 标准化身体状态报告生成器 ⭐ 推荐
- **`scripts/intervals_api.py`**: 用于与 intervals.icu API 交互的 Python 脚本
- **`scripts/fitness_planner.py`**: 用于生成训练计划的 Python 脚本
- **`assets/config_template.json`**: 配置文件模板
