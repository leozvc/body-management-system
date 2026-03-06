# 🏋️ Body Management System - OpenClaw Skills

> One-click deployment for personal health and fat loss management

---

## 🚀 5-Minute Quick Install

### Prerequisites

- ✅ Registered [intervals.icu](https://intervals.icu) account with Garmin/Strava linked
- ✅ OpenClaw installed (`npm install -g openclaw`)
- ✅ Python 3.10+

### One-Click Install

```bash
# 1. Enter skill directory
cd ~/.openclaw/workspace/skills/body-management

# 2. Run install script
chmod +x install.sh
./install.sh
```

### Follow Prompts

Script will guide you to input:
1. **intervals.icu API Key** - Get from Settings → API → Password field
2. **Athlete ID** - Format: `i206099` (i + numbers)
3. **Telegram Group ID** (optional) - For group reminders, skip for private chat

### After Installation

Send in OpenClaw chat:
```
查看我今天的身体状态
```

---

## 📦 Included Skills

| Skill | Function |
|-------|----------|
| `meal-to-intervals` | Sync diet records to intervals.icu |
| `intervals-status-reporter` | Body status analysis & training recommendations |

---

## 📱 Common Commands

| Scenario | Send Message |
|----------|--------------|
| Check body status | "查看我今天的身体状态" |
| Log diet | "早餐吃了 XXX，记录一下" |
| Training decision | "我今天适合打网球吗" |
| List skills | `openclaw skills list` |
| List cron jobs | `openclaw cron list` |

---

## 📚 Detailed Docs

- **Features**: `../../body-management-system.md`
- **Deployment Checklist**: `../../body-management-deployment-checklist.md`

---

## ❓ FAQ

**Q: Where to get API Key?**  
A: Login intervals.icu → Avatar → Settings → API → Copy Password field

**Q: Athlete ID format?**  
A: `i` + numbers, e.g., `i206099`

**Q: Installation failed?**  
A: Run `./install.sh` - it will validate and show error details

---

**Version:** 1.0.0  
**Updated:** 2026-03-06
