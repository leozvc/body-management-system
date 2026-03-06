#!/bin/bash
# 🏋️ Body Management System - One-Click Install Script
# Purpose: Deploy body management skills in OpenClaw

set -e

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print functions
print_header() {
    echo -e "\n${BLUE}════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}════════════════════════════════════════${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "  $1"
}

# Check prerequisites
check_prerequisites() {
    print_header "Step 0: Check Prerequisites"
    
    # Check OpenClaw
    if command -v openclaw &> /dev/null; then
        print_success "OpenClaw installed: $(openclaw --version)"
    else
        print_error "OpenClaw not installed"
        print_info "Please run: npm install -g openclaw"
        exit 1
    fi
    
    # Check Gateway status
    if openclaw gateway status | grep -q "running"; then
        print_success "OpenClaw Gateway is running"
    else
        print_warning "Gateway not running, attempting to start..."
        openclaw gateway start
        sleep 3
    fi
    
    # Check Python
    if command -v python3 &> /dev/null; then
        print_success "Python3 installed: $(python3 --version)"
    else
        print_error "Python3 not installed"
        print_info "Please install Python 3.10+"
        exit 1
    fi
    
    # Check requests library
    if python3 -c "import requests" 2>/dev/null; then
        print_success "Python requests library installed"
    else
        print_warning "Installing Python requests library..."
        pip3 install requests --user
    fi
}

# Get user input
get_user_input() {
    print_header "Step 1: Configure intervals.icu Credentials"
    
    echo ""
    print_info "┌─────────────────────────────────────────────┐"
    print_info "│  How to get API Key:                        │"
    print_info "│  1. Visit https://intervals.icu             │"
    print_info "│  2. Login to your account                   │"
    print_info "│  3. Click Avatar → Settings → API           │"
    print_info "│  4. Copy the 'Password' field value         │"
    print_info "│     (NOT the username)                      │"
    print_info "└─────────────────────────────────────────────┘"
    echo ""
    
    read -p "Enter intervals.icu API Key: " API_KEY
    read -p "Enter Athlete ID (i.e., i206099): " ATHLETE_ID
    
    # Validate input format
    if [[ ! "$ATHLETE_ID" =~ ^i[0-9]+$ ]]; then
        print_error "Invalid Athlete ID format. Should be i + numbers (e.g., i206099)"
        exit 1
    fi
    
    print_success "Credentials received"
    print_info "API Key: ${API_KEY:0:10}... (hidden)"
    print_info "Athlete ID: $ATHLETE_ID"
}

# Create config file
create_config() {
    print_header "Step 2: Create Configuration File"
    
    CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    CONFIG_FILE="$CONFIG_DIR/config.json"
    
    cat > "$CONFIG_FILE" << EOF
{
  "intervals_icu": {
    "api_key": "$API_KEY",
    "athlete_id": "$ATHLETE_ID"
  },
  "fitness_goals": {
    "primary_goal": "weight_loss",
    "training_days_per_week": 5
  }
}
EOF
    
    print_success "Config file created: $CONFIG_FILE"
    
    # Copy to skill directories
    if [ -d "$CONFIG_DIR/meal-to-intervals" ]; then
        cp "$CONFIG_FILE" "$CONFIG_DIR/meal-to-intervals/config.json"
        print_success "Copied to meal-to-intervals skill directory"
    fi
    
    if [ -d "$CONFIG_DIR/intervals-status-reporter" ]; then
        cp "$CONFIG_FILE" "$CONFIG_DIR/intervals-status-reporter/config.json"
        print_success "Copied to intervals-status-reporter skill directory"
    fi
}

# Validate API credentials
validate_credentials() {
    print_header "Step 3: Validate API Credentials"
    
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    TEST_SCRIPT="$SCRIPT_DIR/intervals-status-reporter/scripts/intervals_api.py"
    
    if [ ! -f "$TEST_SCRIPT" ]; then
        print_error "Test script not found: $TEST_SCRIPT"
        exit 1
    fi
    
    print_info "Testing intervals.icu API connection..."
    
    # Run test
    if python3 "$TEST_SCRIPT" --action get_summary_data > /tmp/intervals_test.json 2>&1; then
        print_success "API credentials validated!"
        
        # Show brief info
        if command -v jq &> /dev/null; then
            print_info "Athlete ID: $(jq -r '.athlete_summary[0].athlete_id' /tmp/intervals_test.json 2>/dev/null || echo "N/A")"
            print_info "CTL: $(jq -r '.athlete_summary[0].fitness' /tmp/intervals_test.json 2>/dev/null || echo "N/A")"
            print_info "ATL: $(jq -r '.athlete_summary[0].fatigue' /tmp/intervals_test.json 2>/dev/null || echo "N/A")"
            print_info "TSB: $(jq -r '.athlete_summary[0].form' /tmp/intervals_test.json 2>/dev/null || echo "N/A")"
        fi
    else
        print_error "API credentials validation failed"
        print_info "Error details:"
        cat /tmp/intervals_test.json | head -20
        echo ""
        print_info "Possible causes:"
        print_info "  1. Wrong API Key (should be Password field, not username)"
        print_info "  2. Invalid Athlete ID format (should be i + numbers)"
        print_info "  3. Network connection issue"
        exit 1
    fi
    
    rm -f /tmp/intervals_test.json
}

# Install skills
install_skills() {
    print_header "Step 4: Install Skills to OpenClaw"
    
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Install meal-to-intervals
    if [ -d "$SCRIPT_DIR/meal-to-intervals" ]; then
        print_info "Installing meal-to-intervals skill..."
        if openclaw skills install "$SCRIPT_DIR/meal-to-intervals"; then
            print_success "meal-to-intervals installed successfully"
        else
            print_error "meal-to-intervals installation failed"
            exit 1
        fi
    else
        print_warning "meal-to-intervals directory not found, skipping"
    fi
    
    # Install intervals-status-reporter
    if [ -d "$SCRIPT_DIR/intervals-status-reporter" ]; then
        print_info "Installing intervals-status-reporter skill..."
        if openclaw skills install "$SCRIPT_DIR/intervals-status-reporter"; then
            print_success "intervals-status-reporter installed successfully"
        else
            print_error "intervals-status-reporter installation failed"
            exit 1
        fi
    else
        print_warning "intervals-status-reporter directory not found, skipping"
    fi
    
    # Verify installation
    print_info "Verifying skill installation..."
    if openclaw skills list | grep -q "meal-to-intervals"; then
        print_success "meal-to-intervals is installed"
    fi
    
    if openclaw skills list | grep -q "intervals-status-reporter"; then
        print_success "intervals-status-reporter is installed"
    fi
}

# Setup CRON jobs (optional)
setup_cron() {
    print_header "Step 5: Setup Scheduled Tasks (Optional)"
    
    echo ""
    read -p "Setup daily 06:00 diet target reminder? (y/n): " SETUP_CRON
    
    if [[ "$SETUP_CRON" =~ ^[Yy]$ ]]; then
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        CRON_FILE="$SCRIPT_DIR/cron-daily-diet.json"
        
        read -p "Enter Telegram Group ID (e.g., -5168006012, skip for private chat): " GROUP_ID
        
        if [ -z "$GROUP_ID" ]; then
            print_info "Skipping group chat config, CRON will run in private chat"
            DELIVERY_CONFIG='"mode": "none"'
        else
            DELIVERY_CONFIG='"mode": "announce", "channel": "telegram", "to": "'$GROUP_ID'"'
        fi
        
        cat > "$CRON_FILE" << EOF
{
  "name": "Daily Diet Target Reminder",
  "schedule": {
    "kind": "cron",
    "expr": "0 6 * * *",
    "tz": "Asia/Shanghai"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "[Diet Target Reminder] Generate today's fat loss diet plan and send: 1. Target calorie intake 2. Macro distribution 3. Meal schedule",
    "timeoutSeconds": 60
  },
  "sessionTarget": "isolated",
  "delivery": {$DELIVERY_CONFIG}
}
EOF
        
        print_info "Installing CRON job..."
        if openclaw cron add "$CRON_FILE"; then
            print_success "CRON job installed"
            print_info "Job name: Daily Diet Target Reminder"
            print_info "Schedule: Daily at 06:00 (Asia/Shanghai)"
        else
            print_warning "CRON job installation failed, can configure manually later"
        fi
    else
        print_info "Skipping CRON setup"
    fi
}

# Show usage guide
show_usage_guide() {
    print_header "🎉 Installation Complete!"
    
    echo ""
    print_success "Body Management System is ready"
    echo ""
    
    print_info "┌─────────────────────────────────────────────┐"
    print_info "│  📱 Quick Start Guide                       │"
    print_info "├─────────────────────────────────────────────┤"
    print_info "│                                             │"
    print_info "│  1️⃣  Check body status:                     │"
    print_info "│     Send: "查看我今天的身体状态"           │"
    print_info "│                                             │"
    print_info "│  2️⃣  Log diet:                              │"
    print_info "│     Send: "早餐吃了一个鸡蛋和面包，记录一下" │"
    print_info "│                                             │"
    print_info "│  3️⃣  Training decision:                     │"
    print_info "│     Send: "我今天适合打网球吗"             │"
    print_info "│                                             │"
    print_info "│  4️⃣  List installed skills:                 │"
    print_info "│     openclaw skills list                    │"
    print_info "│                                             │"
    print_info "│  5️⃣  List CRON jobs:                        │"
    print_info "│     openclaw cron list                      │"
    print_info "│                                             │"
    print_info "└─────────────────────────────────────────────┘"
    echo ""
    
    print_info "┌─────────────────────────────────────────────┐"
    print_info "│  📚 Documentation                           │"
    print_info "├─────────────────────────────────────────────┤"
    print_info "│  • Features: body-management-system.md      │"
    print_info "│  • Deployment: body-management-deployment-  │"
    print_info "│    checklist.md                             │"
    print_info "│  • GitHub: [TODO]                           │"
    print_info "└─────────────────────────────────────────────┘"
    echo ""
    
    print_warning "Tip: If this is your first time, try testing it"
    print_info "Send in OpenClaw chat: 查看我今天的身体状态"
    echo ""
}

# Main function
main() {
    print_header "🏋️ Body Management System - Installation Wizard"
    
    check_prerequisites
    get_user_input
    create_config
    validate_credentials
    install_skills
    setup_cron
    show_usage_guide
    
    print_success "All steps completed!"
}

# Run main function
main "$@"
