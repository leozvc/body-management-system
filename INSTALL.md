# 🏋️ Body Management System - Installation Guide

## 🚀 One-Command Install

```bash
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/setup.sh | bash
```

**Note:** This script requires:
- OpenClaw installed (`npm install -g openclaw`)
- Python 3.10+
- intervals.icu account

---

## 📋 Manual Installation

### Step 1: Clone Repository

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git
```

### Step 2: Configure API Credentials

Create `config.json` in the skills directory:

```bash
cd body-management
cat > config.json << 'EOF'
{
  "intervals_icu": {
    "api_key": "YOUR_API_KEY_HERE",
    "athlete_id": "i206099"
  },
  "fitness_goals": {
    "primary_goal": "weight_loss",
    "training_days_per_week": 5
  }
}
EOF
```

**Get your API credentials:**
1. Login to https://intervals.icu
2. Go to Settings → API
3. Copy the **Password** field (this is your API key)
4. Your Athlete ID is in the URL (e.g., `i206099`)

### Step 3: Copy Config to Skills

```bash
# Copy to meal-to-intervals
cp config.json skills/meal-to-intervals/config.json

# Copy to intervals-status-reporter
cp config.json skills/intervals-status-reporter/config.json
```

### Step 4: Install Python Dependencies

```bash
pip3 install requests --user
```

### Step 5: Install Skills to OpenClaw

```bash
# Install meal-to-intervals
openclaw skills enable meal-to-intervals

# Install intervals-status-reporter
openclaw skills enable intervals-status-reporter
```

**Note:** You may need to restart OpenClaw gateway:
```bash
openclaw gateway restart
```

### Step 6: Verify Installation

```bash
# Check skills are installed
openclaw skills list | grep -E "meal|intervals"

# Test body status report
cd skills/intervals-status-reporter
python3 scripts/body_status_report.py
```

If you see a formatted report, installation is successful! ✅

---

## ⚙️ Optional: Setup Daily Reminders

To receive daily diet target reminders at 06:00:

```bash
openclaw cron add cron-daily-diet.json
```

Verify:
```bash
openclaw cron list
```

---

## 🎯 Quick Start

After installation, send in OpenClaw chat:

```
查看我今天的身体状态
```

You should receive a complete body status report!

---

## 📚 Usage Examples

See [USAGE_PROMPTS.md](USAGE_PROMPTS.md) for:
- Common commands
- Example conversations
- Pro tips
- Troubleshooting

---

## 🐛 Troubleshooting

### Issue: "API credentials validation failed"

**Solution:**
1. Verify API Key is the **Password** field (not username)
2. Verify Athlete ID format: `i` + numbers (e.g., `i206099`)
3. Test connection:
   ```bash
   cd skills/intervals-status-reporter
   python3 scripts/intervals_api.py --action get_summary_data
   ```

### Issue: "Skills not found"

**Solution:**
1. Check skills directory:
   ```bash
   ls ~/.openclaw/workspace/skills/
   ```
2. Verify skills are in correct location:
   ```bash
   ls ~/.openclaw/workspace/skills/body-management/skills/
   ```
3. Restart gateway:
   ```bash
   openclaw gateway restart
   ```

### Issue: "Python requests not installed"

**Solution:**
```bash
pip3 install requests --user
```

---

## 📞 Support

- **GitHub Issues**: https://github.com/leozvc/body-management-system/issues
- **Usage Prompts**: [USAGE_PROMPTS.md](USAGE_PROMPTS.md)
- **Features**: [body-management-system.md](../../body-management-system.md)

---

**Version:** 1.0.0  
**Last Updated:** 2026-03-06
