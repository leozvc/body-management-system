# 🏋️ Body Management System

> Automated health tracking and training recommendations for OpenClaw

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/powered%20by-OpenClaw-orange.svg)](https://openclaw.ai)

---

## 🚀 Quick Install

### Option 1: One-Command Install (Recommended)

```bash
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/setup.sh | bash
```

### Option 2: Manual Install

```bash
# Clone repository
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git

# Follow detailed instructions
cat body-management/INSTALL.md
```

---

## 📋 Prerequisites

- **OpenClaw**: `npm install -g openclaw`
- **Python 3.10+**
- **intervals.icu** account ([register](https://intervals.icu))

---

## 🎯 What You Get

### Skills Included

| Skill | Description |
|-------|-------------|
| **meal-to-intervals** | Auto-log meals to intervals.icu with calculated macros |
| **intervals-status-reporter** | Generate standardized body status reports |

### Features

- ✅ **Automated Diet Logging** - Text input, auto-sync to intervals.icu
- ✅ **Body Status Analysis** - HRV, sleep, training load, fatigue
- ✅ **Smart Recommendations** - Training advice based on your data
- ✅ **Daily Reminders** - Optional 06:00 diet target notifications
- ✅ **Privacy First** - Data stays in your intervals.icu account

---

## 📱 Quick Start

After installation, send in OpenClaw chat:

```
查看我今天的身体状态
```

You'll get:
```
📊 身体状态报告
日期：2026-03-06

═══ 核心指标 ═══
✅ 静息心率：56 bpm
✅ HRV: 62 ms
⚠️ 睡眠：5h 48m

═══ 训练负荷 ═══
CTL: 18.0 (体能)
ATL: 25.3 (疲劳)
TSB: -7.3 (轻度疲劳)

═══ 训练建议 ═══
✅ 推荐：Zone 1-2 低强度训练
⚠️ 避免：高强度间歇
```

---

## 📚 Documentation

| File | Description |
|------|-------------|
| **[INSTALL.md](INSTALL.md)** | Detailed installation guide |
| **[USAGE_PROMPTS.md](USAGE_PROMPTS.md)** | Copy-paste prompts & examples |
| **[body-management-system.md](../../body-management-system.md)** | Full feature overview |
| **[body-management-deployment-checklist.md](../../body-management-deployment-checklist.md)** | Deployment checklist |

---

## 💡 Common Commands

### Body Status
```
查看我今天的身体状态
```

### Log Meals
```
早餐吃了一个鸡蛋和面包，记录一下
午餐：鸡胸肉 200g，米饭 150g，西兰花
```

### Training Decisions
```
我今天适合打网球吗
最近训练负荷怎么样
我恢复好了吗
```

### System Commands
```
openclaw skills list
openclaw cron list
```

---

## 🎓 Example Usage

See **[USAGE_PROMPTS.md](USAGE_PROMPTS.md)** for:
- ✅ Complete prompt library
- ✅ Example conversations
- ✅ Pro tips & workflows
- ✅ Troubleshooting guide

---

## 📦 Project Structure

```
body-management-system/
├── skills/
│   ├── meal-to-intervals/          # Diet logging skill
│   └── intervals-status-reporter/  # Body status analysis skill
├── config.json                     # API credentials (create from template)
├── cron-daily-diet.json            # Daily reminder template
├── setup.sh                        # One-click installer
├── INSTALL.md                      # Installation guide ⭐
├── USAGE_PROMPTS.md                # Usage examples ⭐
├── README.md                       # This file
└── LICENSE                         # MIT License
```

---

## 🔧 Configuration

### Setup API Credentials

1. Get intervals.icu API key:
   - Login to https://intervals.icu
   - Settings → API → Copy **Password** field

2. Create `config.json`:
   ```json
   {
     "intervals_icu": {
       "api_key": "YOUR_API_KEY",
       "athlete_id": "i206099"
     }
   }
   ```

3. Copy to skill directories:
   ```bash
   cp config.json skills/meal-to-intervals/
   cp config.json skills/intervals-status-reporter/
   ```

---

## 🐛 Troubleshooting

**Problem: Skills not working**

```bash
# Check installation
openclaw skills list

# Test API connection
cd skills/intervals-status-reporter
python3 scripts/body_status_report.py
```

**Problem: API authentication failed**

- Verify API key is the **Password** field (not username)
- Verify Athlete ID format: `i` + numbers

See **[INSTALL.md](INSTALL.md)** for detailed troubleshooting.

---

## 📞 Support

- **Issues**: https://github.com/leozvc/body-management-system/issues
- **Discussions**: https://github.com/leozvc/body-management-system/discussions

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file.

---

**Version:** 1.0.0  
**Author:** leozvc  
**Last Updated:** 2026-03-06
