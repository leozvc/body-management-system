#!/usr/bin/env python3
"""
身体状态报告生成器
基于 intervals.icu 数据生成标准化的身体状态报告
"""

import json
import os
import sys
from datetime import datetime
from intervals_api import get_summary_data, load_config

# 状态评估阈值
HRV_THRESHOLDS = {
    'excellent': 80,
    'good': 50,
    'fair': 30,
    'poor': 0
}

SLEEP_THRESHOLDS = {
    'excellent': 8 * 3600,  # 8 小时
    'good': 7 * 3600,       # 7 小时
    'fair': 6 * 3600,       # 6 小时
    'poor': 0
}

TSB_THRESHOLDS = {
    'excellent': 10,
    'good': 0,
    'fatigue': -10,
    'overreached': -20
}

RHR_THRESHOLDS = {
    'excellent': 50,
    'good': 60,
    'fair': 70,
    'poor': 100
}


def get_status_icon(value, thresholds, higher_is_better=True):
    """根据阈值获取状态图标"""
    if higher_is_better:
        if value >= thresholds['excellent']:
            return '✅'
        elif value >= thresholds['good']:
            return '✅'
        elif value >= thresholds['fair']:
            return '⚠️'
        else:
            return '❌'
    else:
        # 越低越好（如静息心率）
        if value <= thresholds['excellent']:
            return '✅'
        elif value <= thresholds['good']:
            return '✅'
        elif value <= thresholds['fair']:
            return '⚠️'
        else:
            return '❌'


def get_tsb_status(tsb):
    """获取 TSB 状态描述"""
    if tsb >= 10:
        return '🟢 状态极佳', '适合高强度训练/比赛'
    elif tsb >= 0:
        return '🟢 状态良好', '适合正常训练'
    elif tsb >= -10:
        return '🟡 轻度疲劳', '建议中等强度训练'
    elif tsb >= -20:
        return '🟠 疲劳累积', '建议恢复训练或休息'
    else:
        return '🔴 过度疲劳', '强制休息，避免训练'


def format_duration(seconds):
    """将秒数格式化为 Xh Xm"""
    if seconds is None:
        return 'N/A'
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}m"


def generate_report(data=None):
    """生成标准化身体状态报告"""
    
    # 获取数据
    if data is None:
        data = get_summary_data()
    
    today_wellness = data.get('today_wellness', {})
    
    # athlete_summary 可能是数组（按日期分组）或字典
    athlete_summary_raw = data.get('athlete_summary', [])
    if isinstance(athlete_summary_raw, list) and len(athlete_summary_raw) > 0:
        # 取最新一天的数据（第一个元素）
        athlete_summary = athlete_summary_raw[0]
    else:
        athlete_summary = athlete_summary_raw
    
    recent_activities = data.get('recent_activities', [])
    
    # 提取关键指标
    rhr = today_wellness.get('restingHR') or athlete_summary.get('resting_hr', 0)
    hrv = today_wellness.get('hrv') or 0
    sleep_secs = today_wellness.get('sleepSecs') or 0
    sleep_score = today_wellness.get('sleepScore') or 0
    
    ctl = athlete_summary.get('ctl', 0)
    atl = athlete_summary.get('atl', 0)
    tsb = athlete_summary.get('form', 0)  # form = TSB
    
    kcal_consumed = today_wellness.get('kcalConsumed', 0)
    protein = today_wellness.get('protein', 0)
    fat = today_wellness.get('fatTotal', 0)
    carbs = today_wellness.get('carbohydrates', 0)
    steps = today_wellness.get('steps', 0)
    
    # 生成报告
    report = []
    report.append("")
    report.append("📊 身体状态报告")
    report.append(f"**日期**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")
    
    # ═══ 核心指标 ═══
    report.append("═══ 核心指标 ═══")
    report.append("")
    
    # 静息心率
    rhr_icon = get_status_icon(rhr, RHR_THRESHOLDS, higher_is_better=False)
    report.append(f"{rhr_icon} **静息心率**: {rhr} bpm")
    
    # HRV
    hrv_icon = get_status_icon(hrv, HRV_THRESHOLDS)
    report.append(f"{hrv_icon} **HRV**: {hrv} ms")
    
    # 睡眠
    sleep_icon = get_status_icon(sleep_secs, SLEEP_THRESHOLDS)
    sleep_str = format_duration(sleep_secs)
    report.append(f"{sleep_icon} **睡眠**: {sleep_str} (评分：{sleep_score})")
    
    report.append("")
    
    # ═══ 训练负荷 ═══
    report.append("═══ 训练负荷 ═══")
    report.append("")
    report.append(f"**CTL** (体能): {ctl:.1f}")
    report.append(f"**ATL** (疲劳): {atl:.1f}")
    
    tsb_status, tsb_advice = get_tsb_status(tsb)
    report.append(f"**TSB** (状态): {tsb:.1f} - {tsb_status}")
    report.append("")
    
    # ═══ 近期运动 ═══
    report.append("═══ 近期运动 ═══")
    report.append("")
    
    if recent_activities and len(recent_activities) > 0:
        # 表头
        report.append("| 日期 | 类型 | 时长 | 热量 | 平均心率 |")
        report.append("|------|------|------|--------|----------|")
        
        # 最近 5 次运动
        for activity in recent_activities[:5]:
            date = activity.get('start_date_local', 'N/A')[:10]
            act_type = activity.get('type', 'Unknown')
            moving_time = format_duration(activity.get('moving_time', 0))
            calories = activity.get('calories', 0)
            avg_hr = activity.get('average_heartrate', 'N/A')
            
            report.append(f"| {date} | {act_type} | {moving_time} | {calories} kcal | {avg_hr} bpm |")
    else:
        report.append("近期无运动记录")
    
    report.append("")
    
    # ═══ 今日摄入 ═══
    report.append("═══ 今日摄入 ═══")
    report.append("")
    report.append(f"🔥 **热量**: {kcal_consumed:.0f} kcal")
    report.append(f"🍞 **碳水**: {carbs:.1f}g")
    report.append(f"💪 **蛋白质**: {protein:.1f}g")
    report.append(f"🥑 **脂肪**: {fat:.1f}g")
    report.append(f"👣 **步数**: {steps:,} 步")
    report.append("")
    
    # ═══ 训练建议 ═══
    report.append("═══ 训练建议 ═══")
    report.append("")
    report.append(f"💡 **状态**: {tsb_advice}")
    report.append("")
    
    # 根据 TSB 给出具体建议
    if tsb >= 10:
        report.append("✅ **推荐**:")
        report.append("- 高强度间歇训练 (HIIT)")
        report.append("- 比赛/测试")
        report.append("- 大重量力量训练")
        report.append("")
        report.append("⚠️ **注意**:")
        report.append("- 状态虽好但避免连续高强度")
        
    elif tsb >= 0:
        report.append("✅ **推荐**:")
        report.append("- 正常强度训练")
        report.append("- 技术练习")
        report.append("- 中等强度有氧")
        report.append("")
        report.append("⚠️ **注意**:")
        report.append("- 监控疲劳累积")
        
    elif tsb >= -10:
        report.append("✅ **推荐**:")
        report.append("- Zone 1-2 低强度训练")
        report.append("- 技术练习（不拼强度）")
        report.append("- 主动恢复（散步/瑜伽）")
        report.append("")
        report.append("⚠️ **避免**:")
        report.append("- 高强度间歇")
        report.append("- 长时间耐力训练")
        report.append("- 力竭训练")
        
    else:
        report.append("✅ **推荐**:")
        report.append("- 完全休息")
        report.append("- 轻度活动（散步/拉伸）")
        report.append("- 保证睡眠 8h+")
        report.append("")
        report.append("⚠️ **避免**:")
        report.append("- 任何正式训练")
        report.append("- 长时间站立/行走")
    
    report.append("")
    
    # ═══ 恢复建议 ═══
    report.append("═══ 恢复建议 ═══")
    report.append("")
    
    suggestions = []
    
    if sleep_secs < 7 * 3600:
        suggestions.append("😴 **优先补觉** - 昨晚睡眠不足，今晚目标 8h")
    
    if hrv < 50:
        suggestions.append("🧘 **压力管理** - HRV 偏低，建议冥想/深呼吸")
    
    if tsb < -10:
        suggestions.append("🛀 **主动恢复** - 热水澡/按摩/泡沫轴")
    
    if kcal_consumed < 1000 and datetime.now().hour < 18:
        suggestions.append("🍽 **营养补充** - 今日摄入偏低，注意按时进餐")
    
    if not suggestions:
        suggestions.append("✨ 状态良好，保持当前节奏！")
    
    for suggestion in suggestions:
        report.append(suggestion)
    
    report.append("")
    report.append("---")
    report.append(f"*数据来自 intervals.icu | 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    
    return "\n".join(report)


def main():
    """主函数"""
    try:
        report = generate_report()
        print(report)
    except Exception as e:
        print(f"❌ 生成报告失败：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
