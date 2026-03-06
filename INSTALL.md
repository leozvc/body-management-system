# 🏋️ Body Management System - Interactive Install

> **Copy and paste this URL into your OpenClaw chat to start interactive installation**

**中文用户:** 使用 [INSTALL.zh-CN.md](INSTALL.zh-CN.md) 获取中文安装指南

---

## 🚀 Install in OpenClaw Chat

**Step 1:** Copy this command:

```
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/INSTALL.md
```

**Step 2:** Paste into your OpenClaw chat and send

**Step 3:** Follow the interactive prompts!

---

## ⭐ Star the Project

If this project helps you:

1. **Star on GitHub** - https://github.com/leozvc/body-management-system
2. **Share with friends** - Help more fitness enthusiasts
3. **Submit feedback** - Open an issue with suggestions

Your support drives continuous improvement! 🙏

---

## 🔄 Version Check & Upgrade

Every time you run the install command, the system will:

1. ✅ Check local version
2. ✅ Check GitHub latest version
3. ✅ Prompt if update is available

### Version Check Flow

```
📦 Version Check

Local version: 1.0.0
Latest version: 1.1.0

New version available! Update now?
[y/n]: y

Updating...
✅ Update complete!
```

### Manual Update Check

```bash
cd ~/.openclaw/workspace/skills/body-management
git pull origin main
cat VERSION
```

---

## 📋 Installation Steps

### 1️⃣ Credential Collection
```
Agent: I'll help you install the Body Management System.

First, I need your intervals.icu API credentials:
1. API Key (from Settings → API → Password field)
2. Athlete ID (format: i206099)

To get these:
1. Visit https://intervals.icu
2. Login → Settings → API
3. Copy the "Password" value
```

### 2️⃣ Create Data Directory
```
Agent: Creating your data directory...

Location: ~/.openclaw/workspace/body-management-data/

This is where YOUR data will be stored:
- Meal records
- Wellness data
- API configuration

✅ Data directory created
```

### 3️⃣ Repository Setup
```
Agent: Cloning repository...
✅ Repository cloned to ~/.openclaw/workspace/skills/body-management
```

### 4️⃣ Configuration
```
Agent: Creating configuration in your data directory...
✅ Config saved to: ~/.openclaw/workspace/body-management-data/config.json
```

### 5️⃣ Connection Test
```
Agent: Testing API connection...
✅ Connection successful! Welcome, [Your Name]
```

### 6️⃣ Skill Installation
```
Agent: Enabling skills...
✅ meal-to-intervals installed
✅ intervals-status-reporter installed
```

### 7️⃣ Completion
```
Agent: 🎉 Installation Complete!

Your data will be stored in:
~/.openclaw/workspace/body-management-data/

Try it now: Send "查看我今天的身体状态"
```

---

## 🎯 Quick Reference

### Get Your API Credentials

| Step | Action |
|------|--------|
| 1 | Visit https://intervals.icu |
| 2 | Login to your account |
| 3 | Click avatar → Settings → API |
| 4 | Copy the **Password** field (API Key) |
| 5 | Note your Athlete ID from URL (e.g., i206099) |

### Common Commands After Install

```
查看我今天的身体状态          # Get body status report
早餐吃了 XXX，记录一下         # Log a meal
我今天适合打网球吗            # Training recommendation
openclaw skills list          # List installed skills
```

---

## 📦 What Gets Installed

### Your Data Directory (Created)
```
~/.openclaw/workspace/body-management-data/
├── config.json              # Your API credentials ⭐
├── meals/                   # Meal logging records
├── wellness/                # Wellness tracking data
└── logs/                    # Operation logs
```

### Skills Directory (Read-Only)
```
~/.openclaw/workspace/skills/body-management/
├── skills/                  # Skill code
├── scripts/                 # Installation scripts
├── docs/                    # Documentation
└── ...
```

**Important:** 
- ✅ Your data is in `body-management-data/` (backup this!)
- ❌ Don't modify files in `skills/body-management/`

---

## 🔧 Manual Installation (Alternative)

If interactive install doesn't work:

```bash
# 1. Create data directory
mkdir -p ~/.openclaw/workspace/body-management-data

# 2. Clone repository
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git

# 3. Create config in data directory
cat > ~/.openclaw/workspace/body-management-data/config.json << 'EOF'
{
  "intervals_icu": {
    "api_key": "YOUR_API_KEY",
    "athlete_id": "i206099"
  }
}
EOF

# 4. Test
cd body-management/skills/intervals-status-reporter
python3 scripts/body_status_report.py
```

---

## 🐛 Troubleshooting

**Issue: "API credentials validation failed"**

- Verify API Key is the **Password** field (not username)
- Verify Athlete ID format: `i` + numbers (e.g., i206099)
- Check config location: `~/.openclaw/workspace/body-management-data/config.json`

**Issue: "Skills not found after install"**

```bash
openclaw skills list
openclaw gateway restart
```

**Issue: "How to check for updates"**

```bash
cd ~/.openclaw/workspace/skills/body-management
git pull origin main
cat VERSION
```

**Issue: "Where is my data stored?"**

```bash
# View your data directory
ls -la ~/.openclaw/workspace/body-management-data/

# View meal records
ls -la ~/.openclaw/workspace/body-management-data/meals/
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **INSTALL.md** | English installation guide |
| **INSTALL.zh-CN.md** | 中文安装指南 |
| **DATA_STORAGE.md** | Data storage locations & best practices ⭐ |
| **USAGE_PROMPTS.md** | Copy-paste prompts for common tasks |
| **README.md** | Quick reference and features |

---

## 🔒 Privacy & Security

### What's Stored Where

| Data Type | Location | Sensitive? |
|-----------|----------|------------|
| API Key | `body-management-data/config.json` | 🔴 YES |
| Meal Records | `body-management-data/meals/` | 🟡 Partially |
| Wellness Data | `body-management-data/wellness/` | 🟡 Partially |
| Skill Code | `skills/body-management/` | 🟢 No |

### Security Tips

1. **Never commit** `body-management-data/` to Git
2. **Backup regularly** - Your data is valuable
3. **Check permissions**:
   ```bash
   chmod 700 ~/.openclaw/workspace/body-management-data/
   chmod 600 ~/.openclaw/workspace/body-management-data/config.json
   ```

---

## 📞 Support

- **GitHub Issues**: https://github.com/leozvc/body-management-system/issues
- **Project Home**: https://github.com/leozvc/body-management-system
- **Discussions**: https://github.com/leozvc/body-management-system/discussions

---

## 🌟 Support the Project

If this project helps you:

1. ⭐ **Star on GitHub** - Give us a star
2. 📢 **Share with friends** - Recommend to others
3. 💡 **Submit suggestions** - Open an issue
4. 🔧 **Contribute code** - PRs welcome!

Your support makes the project better! 🙏

---

**Version:** 1.0.0  
**License:** MIT  
**Author:** leozvc  
**Last Updated:** 2026-03-06
