# 📂 Data Storage Guide

> User data is stored in your workspace, NOT in the skills directory.

---

## 🗂️ Storage Locations

### User Data Directory
```
~/.openclaw/workspace/body-management-data/
├── meals/              # Meal logging records
│   ├── 2026-03-06-breakfast.json
│   ├── 2026-03-06-lunch.json
│   └── ...
├── wellness/           # Wellness tracking data
│   ├── 2026-03-06.json
│   └── ...
├── config.json         # Your API configuration
└── logs/               # Operation logs
    └── install.log
```

### Skills Directory (Read-Only)
```
~/.openclaw/workspace/skills/body-management/
├── skills/             # Skill code (DO NOT modify)
├── scripts/            # Installation scripts
├── docs/               # Documentation
└── ...
```

---

## 🔧 Configuration

### First-Time Setup

When you run the installation, the system will:

1. Create data directory:
   ```bash
   mkdir -p ~/.openclaw/workspace/body-management-data
   ```

2. Create config file:
   ```bash
   cat > ~/.openclaw/workspace/body-management-data/config.json << 'EOF'
   {
     "intervals_icu": {
       "api_key": "YOUR_API_KEY",
       "athlete_id": "i206099"
     }
   }
   EOF
   ```

3. Skills will read config from data directory (not from skills/)

---

## 📝 Why Separate Data from Skills?

### Benefits

| Aspect | Old Way (data in skills/) | New Way (data in workspace/) |
|--------|--------------------------|------------------------------|
| **Upgrade Safety** | ❌ Data lost on upgrade | ✅ Data preserved |
| **Backup** | ❌ Hard to find | ✅ Single location |
| **Privacy** | ❌ Mixed with code | ✅ Clear separation |
| **Git** | ❌ Risk of committing data | ✅ Easy to ignore |
| **Multi-user** | ❌ Shared data | ✅ Per-user data |

### Best Practices

```
✅ DO: Store user data in ~/.openclaw/workspace/body-management-data/
✅ DO: Keep skills directory read-only
✅ DO: Backup your data directory regularly
❌ DON'T: Store personal data in skills/ directory
❌ DON'T: Modify skill code files
```

---

## 🔄 Migration (For Existing Users)

If you have data in the old location:

```bash
# 1. Backup old data
cp -r ~/.openclaw/workspace/skills/body-management/skills/meal-to-intervals/*.json /tmp/backup-meals/

# 2. Create new data directory
mkdir -p ~/.openclaw/workspace/body-management-data/meals

# 3. Move data
mv /tmp/backup-meals/*.json ~/.openclaw/workspace/body-management-data/meals/

# 4. Move config
mv ~/.openclaw/workspace/skills/body-management/skills/*/config.json ~/.openclaw/workspace/body-management-data/config.json
```

---

## 🔒 Privacy & Security

### What's Stored

| Data Type | Location | Sensitive? |
|-----------|----------|------------|
| API Key | `body-management-data/config.json` | 🔴 YES |
| Meal Records | `body-management-data/meals/*.json` | 🟡 Partially |
| Wellness Data | `body-management-data/wellness/*.json` | 🟡 Partially |
| Skill Code | `skills/body-management/` | 🟢 No |

### Security Tips

1. **Never commit** `body-management-data/` to Git
2. **Backup regularly** - Your data is valuable
3. **Encrypt backups** - Contains health data
4. **Check permissions**:
   ```bash
   chmod 700 ~/.openclaw/workspace/body-management-data/
   chmod 600 ~/.openclaw/workspace/body-management-data/config.json
   ```

---

## 📊 Directory Structure Overview

```
~/.openclaw/workspace/
├── body-management-data/          ⭐ YOUR DATA (Backup this!)
│   ├── config.json                # API credentials
│   ├── meals/                     # Meal records
│   ├── wellness/                  # Health data
│   └── logs/                      # Operation logs
│
└── skills/
    └── body-management/           🔧 SKILL CODE (Don't modify)
        ├── skills/
        ├── scripts/
        ├── docs/
        └── ...
```

---

## 🛠️ Advanced: Custom Data Location

To use a custom data directory:

1. Create symlink:
   ```bash
   ln -s /your/custom/path ~/.openclaw/workspace/body-management-data
   ```

2. Or set environment variable in skill config (future feature)

---

**Last Updated:** 2026-03-06  
**Version:** 1.0.0
