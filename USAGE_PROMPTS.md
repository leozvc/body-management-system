# 📝 Usage Prompts - Body Management System

> Copy and paste these prompts to get started with your body management system.

---

## 🎯 Quick Start (First Time)

### Check Your Body Status
```
查看我今天的身体状态
```

**What you get:**
- Complete body status report
- HRV, resting heart rate, sleep analysis
- Training load (CTL/ATL/TSB)
- Training recommendations based on fatigue
- Recovery suggestions

---

## 🍽 Diet Logging

### Log a Meal (Text Input)
```
早餐吃了一个鸡蛋和全麦面包，记录一下
```

```
午餐：鸡胸肉 200g，米饭 150g，西兰花 100g
```

```
晚餐吃了三文鱼 250g，红薯 200g，蔬菜沙拉
```

**What happens:**
- Auto-calculates calories and macros
- Syncs to intervals.icu
- Updates daily wellness fields

### Log Water Intake
```
喝了 500ml 水
```

```
今天喝水总量 2000ml
```

---

## 🎾 Training Decisions

### Ask About Today's Training
```
我今天适合打网球吗
```

```
今天适合什么强度的训练？
```

```
我现在的状态能高强度训练吗？
```

**What you get:**
- Recommendation based on TSB (fatigue level)
- Suggested training zones
- What to avoid today

### Ask About Recovery
```
我恢复好了吗？
```

```
最近训练负荷怎么样？
```

```
需要休息吗？
```

---

## 📊 Analysis & Reports

### Get Detailed Analysis
```
生成今日健康报告
```

```
最近 7 天的训练负荷分析
```

```
我的睡眠质量怎么样？
```

### Compare Periods
```
对比上周和本周的训练负荷
```

```
这个月的平均睡眠时长
```

---

## ⚙️ Configuration

### Check Installation
```
openclaw skills list
```

```
openclaw cron list
```

### Update API Credentials
If you need to update your intervals.icu API key:

1. Edit `~/.openclaw/workspace/skills/body-management/config.json`
2. Update `api_key` and `athlete_id`
3. Test with: `查看我今天的身体状态`

---

## 🔧 Troubleshooting Prompts

### If Skills Not Working
```
openclaw skills info meal-to-intervals
```

```
openclaw skills info intervals-status-reporter
```

### Test API Connection
```bash
cd ~/.openclaw/workspace/skills/body-management/skills/intervals-status-reporter
python3 scripts/body_status_report.py
```

### Check Logs
```
openclaw gateway status
```

---

## 💡 Pro Tips

### Daily Routine
**Morning (06:00):**
- Receive automatic diet target reminder (if configured)
- Check today's training recommendation

**Before Meals:**
- Log what you're about to eat for planning
- Or log after eating for tracking

**Before Training:**
- Ask "我今天适合训练吗"
- Get zone recommendations based on fatigue

**Evening:**
- Review daily summary
- Check sleep quality next morning

### Weekly Review
```
最近 7 天的运动记录
```

```
本周平均睡眠和 HRV
```

```
训练负荷是偏高还是偏低？
```

---

## 📚 Example Conversations

### Scenario 1: Morning Check
```
User: 查看我今天的身体状态

Bot: 📊 身体状态报告
     日期：2026-03-06
     静息心率：56 bpm ✅
     HRV: 62 ms ✅
     睡眠：5h 48m ⚠️
     TSB: -7.3 (轻度疲劳)
     
     训练建议：Zone 1-2 低强度训练
     避免：高强度间歇

User: 那我今天还能打网球吗？

Bot: 可以打，但建议：
     - 以技术练习为主
     - 心率控制在 140 以下
     - 避免激烈比赛
```

### Scenario 2: Meal Logging
```
User: 早餐吃了一个麦当劳吉士汉堡，记录一下

Bot: ✅ 已记录到 intervals.icu
     - 热量：303 kcal
     - 蛋白质：15g
     - 脂肪：13g
     - 碳水：33g
     
     今日累计：303 kcal

User: 那我还剩多少热量可以摄入？

Bot: 基于你的减脂目标 (1600 kcal/天):
     剩余：1297 kcal
     
     建议分配:
     - 午餐：600 kcal
     - 晚餐：500 kcal
     - 加餐：197 kcal
```

### Scenario 3: Training Decision
```
User: 我连续打了 3 天网球，今天还要继续吗？

Bot: 查看你的状态...
     
     ⚠️ 建议今天休息或主动恢复
     
     原因:
     - TSB: -7.3 (疲劳累积)
     - 睡眠：5h 48m (不足)
     - 连续 3 天训练
     
     推荐:
     - 完全休息
     - 或 Zone 1 散步 30 分钟
     - 今晚保证 8h 睡眠
```

---

## 🎓 Learning Path

### Week 1: Basics
- Day 1: Install and setup
- Day 2: Log all meals
- Day 3: Check morning body status
- Day 4: Ask training recommendation
- Day 5-7: Build the habit

### Week 2: Optimization
- Review weekly report
- Adjust diet based on data
- Fine-tune training intensity
- Set up automatic reminders

### Week 3+: Advanced
- Analyze trends
- Compare periods
- Optimize recovery
- Share insights with coach

---

**More docs:**
- [INSTALL.md](INSTALL.md) - Installation guide
- [README.md](README.md) - Quick start
- [body-management-system.md](../../body-management-system.md) - Full features
