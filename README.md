# 🏋️ Body Management System

> One-command installation for automated health tracking and training recommendations

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/powered%20by-OpenClaw-orange.svg)](https://openclaw.ai)

---

## 🚀 One-Command Install

```bash
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/setup.sh | bash
```

That's it! ✨

The installer will:
1. ✅ Check prerequisites (OpenClaw, Python)
2. ✅ Download all skills
3. ✅ Guide you through API setup
4. ✅ Install and configure everything

---

## 📋 Prerequisites

- **OpenClaw**: `npm install -g openclaw`
- **Python 3.10+**
- **intervals.icu** account ([register here](https://intervals.icu))

---

## 🎯 Quick Start

After installation, send in OpenClaw chat:

```
查看我今天的身体状态
```

You'll get a complete body status report with:
- ❤️ HRV, resting heart rate, sleep analysis
- 📊 Training load (CTL/ATL/TSB)
- 🎾 Training recommendations
- 🍽 Nutrition tracking

---

## 📦 What's Included

### Skills

| Skill | Description |
|-------|-------------|
| `meal-to-intervals` | Log meals to intervals.icu with auto-calculated macros |
| `intervals-status-reporter` | Generate standardized body status reports |

### Features

- ✅ **Automated Diet Logging** - Text or photo input, auto-sync to intervals.icu
- ✅ **Body Status Analysis** - HRV, sleep, training load, fatigue assessment
- ✅ **Smart Training Recommendations** - Based on your current fatigue level
- ✅ **Daily Reminders** - Optional 06:00 diet target notifications
- ✅ **Privacy First** - All data stays in your intervals.icu account

---

## 📱 Common Commands

| Command | Description |
|---------|-------------|
| `查看我今天的身体状态` | Get today's body status report |
| `早餐吃了 XXX，记录一下` | Log a meal |
| `我今天适合打网球吗` | Get training recommendation |
| `openclaw skills list` | List installed skills |
| `openclaw cron list` | List scheduled reminders |

---

## 📚 Documentation

- **[INSTALL.md](INSTALL.md)** - Detailed installation guide
- **[body-management-system.md](../../body-management-system.md)** - Full feature overview
- **[body-management-deployment-checklist.md](../../body-management-deployment-checklist.md)** - Deployment checklist

---

## 🔧 Manual Installation

```bash
# Clone repository
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git

# Run installer
cd body-management
chmod +x install.sh
./install.sh
```

---

## 🐛 Troubleshooting

**Issue: "API credentials validation failed"**
- Make sure you copied the **Password** field from intervals.icu API settings (not username)
- Athlete ID should be `i` + numbers (e.g., `i206099`)

**Issue: "OpenClaw not found"**
- Run: `npm install -g openclaw`
- Then: `openclaw gateway start`

**Issue: Skills not showing up**
- Run: `openclaw skills list` to verify installation
- Restart gateway: `openclaw gateway restart`

---

## 📞 Support

- **GitHub Issues**: https://github.com/leozvc/body-management-system/issues
- **Documentation**: See `INSTALL.md` and `body-management-system.md`

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Version:** 1.0.0  
**Author:** leozvc  
**Last Updated:** 2026-03-06
