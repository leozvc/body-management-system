# 🏋️ Body Management System

> **Privacy-first** automated health tracking and training recommendations for OpenClaw

[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](CHANGELOG.md)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/powered%20by-OpenClaw-orange.svg)](https://openclaw.ai)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)

---

## ⭐ What's New in v1.1.0

- ✅ Enhanced config validation with helpful error messages
- ✅ Automatic retry logic for transient failures  
- ✅ Structured logging with timestamps
- ✅ Improved privacy protection with comprehensive `.gitignore`
- ✅ Better documentation including CHANGELOG and SECURITY policy

See [CHANGELOG.md](CHANGELOG.md) for full details.

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

### Key Features

- ✅ **Automated Diet Logging** - Text input, auto-sync to intervals.icu
- ✅ **Body Status Analysis** - HRV, sleep, training load, fatigue tracking
- ✅ **Smart Recommendations** - Training advice based on your data
- ✅ **Daily Reminders** - Optional 06:00 diet target notifications
- ✅ **Privacy First** - All data stays on your machine

---

## 📱 Quick Start

After installation, send in OpenClaw chat:

```
查看我今天的身体状态
```

You'll get:
```
📊 身体状态报告
日期：2026-03-08

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

## 🔧 Configuration

### Setup API Credentials

1. **Get intervals.icu API key:**
   - Login to https://intervals.icu
   - Settings → API → Copy **Password** field

2. **Create configuration:**
   ```bash
   # Config will be saved to your data directory
   ~/.openclaw/workspace/body-management-data/config.json
   ```

3. **Verify connection:**
   ```bash
   cd skills/intervals-status-reporter
   python3 scripts/body_status_report.py
   ```

See [INSTALL.md](INSTALL.md) for detailed setup instructions.

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **[INSTALL.md](INSTALL.md)** | Detailed installation guide |
| **[USAGE_PROMPTS.md](USAGE_PROMPTS.md)** | Copy-paste prompts & examples |
| **[DATA_STORAGE.md](../../body-management-data/DATA_STORAGE.md)** | Data storage best practices |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | How to contribute to the project |
| **[SECURITY.md](SECURITY.md)** | Security policy and vulnerability reporting |
| **[CHANGELOG.md](CHANGELOG.md)** | Version history and changes |

---

## 🐛 Troubleshooting

### Common Issues

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
- Verify Athlete ID format: `i` + numbers (e.g., i206099)
- Check internet connection
- See [INSTALL.md](INSTALL.md) for more troubleshooting steps

**Problem: Config validation errors**
- Ensure config.json exists in `~/.openclaw/workspace/body-management-data/`
- Verify both `api_key` and `athlete_id` fields are present
- Check file permissions (should be readable by user)

---

## 🔒 Privacy & Security

Your data is **never** sent to external servers except to intervals.icu:

- ✅ **API keys** stored locally in `body-management-data/config.json`
- ✅ **Meal records** stored in `body-management-data/meals/`
- ✅ **Wellness data** stored in `body-management-data/wellness/`
- ❌ **No data collection** - We don't track or log user information

See [SECURITY.md](SECURITY.md) for our security policy.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Bug report templates
- Feature request guidelines
- Code contribution standards
- Testing requirements

---

## 📞 Support

- **Issues:** https://github.com/leozvc/body-management-system/issues
- **Discussions:** https://github.com/leozvc/body-management-system/discussions
- **Security:** See [SECURITY.md](SECURITY.md)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- **[intervals.icu](https://intervals.icu)** - Excellent health tracking platform
- **[OpenClaw](https://openclaw.ai)** - Powerful automation framework
- **[OpenFoodFacts](https://world.openfoodfacts.org)** - Free nutrition database

---

**Version:** 1.1.0  
**Author:** leozvc  
**Last Updated:** 2026-03-08  
**License:** MIT
