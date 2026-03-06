# Body Management System - Agent Installation Instruction

> This file is designed to be executed by an OpenClaw agent when user requests installation.

---

## 🔄 Version Check (Run First)

Before starting installation, check if update is needed:

```bash
# Check if project exists
if [ -d "~/.openclaw/workspace/skills/body-management/.git" ]; then
  cd ~/.openclaw/workspace/skills/body-management
  
  # Get local version
  LOCAL_VERSION=$(cat VERSION 2>/dev/null || echo "unknown")
  
  # Get remote version (from GitHub)
  REMOTE_VERSION=$(curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/VERSION 2>/dev/null || echo "unknown")
  
  # Compare versions
  if [ "$LOCAL_VERSION" != "$REMOTE_VERSION" ] && [ "$REMOTE_VERSION" != "unknown" ]; then
    echo "📦 Version Check"
    echo ""
    echo "Local version:  $LOCAL_VERSION"
    echo "Latest version: $REMOTE_VERSION"
    echo ""
    echo "New version available! Update now? [y/n]"
    # Wait for user response
  else
    echo "✅ You're running the latest version: $LOCAL_VERSION"
  fi
fi
```

---

## 🎯 Trigger

When user sends any of these in OpenClaw chat:
- "curl https://raw.githubusercontent.com/leozvc/body-management-system/main/INSTALL.md"
- "install body management system"
- "安装肉身管理系统"
- "setup body tracking"

---

## 📋 Agent Action Plan

### Step 1: Acknowledge Request

Respond to user:

```
🏋️ Body Management System Installation

I'll guide you through the installation process. This will:
1. Clone the repository to your skills directory
2. Setup your intervals.icu API credentials
3. Test the connection
4. Enable the skills

Let's get started!

First, I need your intervals.icu API credentials.
```

---

### Step 2: Request API Credentials

Ask user for credentials:

```
📝 Step 1: Get Your intervals.icu API Credentials

Please provide:
1. **API Key** - From intervals.icu Settings → API → Password field
2. **Athlete ID** - Your athlete ID (format: i206099)

To get these:
1. Visit: https://intervals.icu
2. Login → Click your avatar → Settings → API
3. Copy the "Password" value (this is your API Key)
4. Your Athlete ID is in the dashboard URL (e.g., i206099)

Reply with:
API Key: [your key]
Athlete ID: [your ID]
```

---

### Step 3: Clone Repository

Once user provides credentials, execute:

```bash
cd /Users/chichiuliu/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git 2>&1 || echo "Already exists, updating..." && cd body-management && git pull
```

Then respond:
```
✅ Repository cloned/updated successfully!

Location: ~/.openclaw/workspace/skills/body-management
```

---

### Step 4: Create Configuration

Create config file with user's credentials:

```
📝 Step 2: Creating Configuration

Using your provided credentials...
```

Create `config.json`:
```json
{
  "intervals_icu": {
    "api_key": "[USER_API_KEY]",
    "athlete_id": "[USER_ATHLETE_ID]"
  },
  "fitness_goals": {
    "primary_goal": "weight_loss",
    "training_days_per_week": 5
  }
}
```

Then copy to skill directories:
```bash
cp config.json skills/meal-to-intervals/config.json
cp config.json skills/intervals-status-reporter/config.json
```

Respond:
```
✅ Configuration created and copied to skills
```

---

### Step 5: Test API Connection

Test the connection:

```bash
cd skills/intervals-status-reporter
python3 scripts/body_status_report.py 2>&1 | head -20
```

If successful:
```
✅ API connection successful!

Sample data retrieved:
- Athlete: [name]
- CTL: [value]
- ATL: [value]
- TSB: [value]
```

If failed:
```
⚠️ API connection failed. Please check:
1. API Key is correct (Password field, not username)
2. Athlete ID format (i + numbers)
3. Network connection

Error: [error message]

Would you like to try again with different credentials?
```

---

### Step 6: Install Skills

Enable skills in OpenClaw:

```
📦 Step 3: Installing Skills

Enabling meal-to-intervals...
Enabling intervals-status-reporter...
```

Execute:
```bash
openclaw skills list | grep -E "meal|intervals"
```

Respond:
```
✅ Skills installed and ready!

Installed:
- meal-to-intervals
- intervals-status-reporter
```

---

### Step 7: Show Completion

Final message:

```
🎉 Installation Complete!

✅ Body Management System is ready to use!

🚀 Quick Start:
Send me: "查看我今天的身体状态"

📚 Documentation:
- USAGE_PROMPTS.md - Copy-paste prompts
- INSTALL.md - Detailed guide
- README.md - Quick reference

💡 Common Commands:
• "早餐吃了 XXX，记录一下" - Log a meal
• "我今天适合打网球吗" - Training decision
• openclaw skills list - List skills

Enjoy your automated health tracking! 🏋️
```

---

## 🐛 Error Handling

### If git clone fails:
```
⚠️ Repository already exists or git error.

Trying to update existing installation...
[proceed with update]
```

### If API test fails:
```
❌ API connection failed.

Common issues:
1. Wrong API Key (should be Password field)
2. Invalid Athlete ID (should be i + numbers)
3. Network issue

Would you like to:
1. Try again with different credentials
2. Skip test and continue
3. Cancel installation
```

### If skills not found:
```
⚠️ Skills directory not found.

Expected location:
~/.openclaw/workspace/skills/body-management/skills/

Please check if the repository was cloned correctly.
```

---

## 📞 Support References

- GitHub: https://github.com/leozvc/body-management-system
- Issues: https://github.com/leozvc/body-management-system/issues
- Docs: See repository for detailed guides

---

**Instruction Version:** 1.0.0  
**For:** OpenClaw Agent Execution
