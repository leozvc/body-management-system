# 🏋️ Body Management System - One-Click Install

## 🚀 Quick Install (One Command)

```bash
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/setup.sh | bash
```

That's it! The installer will:
1. ✅ Check prerequisites (OpenClaw, Python3)
2. ✅ Download all skills to `~/.openclaw/workspace/skills/`
3. ✅ Guide you through intervals.icu API setup
4. ✅ Install skills to OpenClaw
5. ✅ (Optional) Setup daily diet reminders

---

## 📋 Prerequisites

- **OpenClaw** installed: `npm install -g openclaw`
- **Python 3.10+** installed
- **intervals.icu** account with API key

---

## 🔧 Manual Installation

If you prefer manual setup:

```bash
# 1. Clone the repository
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git

# 2. Run the installer
cd body-management
chmod +x install.sh
./install.sh
```

---

## 📚 What Gets Installed

### Skills
- `meal-to-intervals` - Diet logging to intervals.icu
- `intervals-status-reporter` - Body status analysis

### Tools
- `install.sh` - Interactive installer
- `body_status_report.py` - Standardized report generator
- `cron-daily-diet.json` - Daily reminder template

### Documentation
- `README.md` - Quick start guide
- `INSTALL.md` - This file
- `body-management-system.md` - Full feature overview

---

## 🎯 After Installation

In OpenClaw chat, send:
```
查看我今天的身体状态
```

---

## 📞 Support

- **GitHub Issues**: https://github.com/leozvc/body-management-system/issues
- **Docs**: See project root for detailed guides

---

**Version:** 1.0.0  
**License:** MIT
