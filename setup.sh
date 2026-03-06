#!/bin/bash
# 🏋️ Body Management System - One-Click Setup
# Usage: curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/setup.sh | bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_header() {
    echo -e "\n${BLUE}════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}════════════════════════════════════════${NC}\n"
}

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_info() { echo -e "  $1"; }

# Check prerequisites
check_prerequisites() {
    print_header "Step 0: Checking Prerequisites"
    
    if ! command -v openclaw &> /dev/null; then
        print_error "OpenClaw not installed"
        print_info "Please run: npm install -g openclaw"
        exit 1
    fi
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 not installed"
        exit 1
    fi
    
    if ! python3 -c "import requests" 2>/dev/null; then
        print_warning "Installing Python requests library..."
        pip3 install requests --user -q
    fi
    
    print_success "Prerequisites check passed"
}

# Clone repository
clone_repo() {
    print_header "Step 1: Downloading Project"
    
    SKILLS_DIR="$HOME/.openclaw/workspace/skills"
    PROJECT_DIR="$SKILLS_DIR/body-management"
    REPO_URL="https://github.com/leozvc/body-management-system.git"
    
    if [ -d "$PROJECT_DIR/.git" ]; then
        print_info "Repository exists, updating..."
        cd "$PROJECT_DIR"
        git pull origin main
    else
        print_info "Cloning repository..."
        mkdir -p "$SKILLS_DIR"
        cd "$SKILLS_DIR"
        git clone "$REPO_URL" body-management
        cd "$PROJECT_DIR"
    fi
    
    print_success "Project downloaded: $PROJECT_DIR"
}

# Setup config
setup_config() {
    print_header "Step 2: Configuring API Credentials"
    
    print_info "┌─────────────────────────────────────────────┐"
    print_info "│  Get your intervals.icu API credentials:    │"
    print_info "│  1. Visit https://intervals.icu             │"
    print_info "│  2. Login → Settings → API                  │"
    print_info "│  3. Copy the 'Password' field (API Key)     │"
    print_info "│  4. Your Athlete ID is in the URL           │"
    print_info "└─────────────────────────────────────────────┘"
    echo ""
    
    read -p "Enter intervals.icu API Key: " API_KEY
    read -p "Enter Athlete ID (e.g., i206099): " ATHLETE_ID
    
    # Validate format
    if [[ ! "$ATHLETE_ID" =~ ^i[0-9]+$ ]]; then
        print_error "Invalid Athlete ID format"
        exit 1
    fi
    
    # Create config
    cat > config.json << EOF
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
    
    # Copy to skills
    cp config.json skills/meal-to-intervals/config.json
    cp config.json skills/intervals-status-reporter/config.json
    
    print_success "Configuration created"
}

# Test connection
test_connection() {
    print_header "Step 3: Testing API Connection"
    
    cd skills/intervals-status-reporter
    
    if python3 scripts/body_status_report.py > /tmp/test_report.txt 2>&1; then
        print_success "API connection successful!"
        print_info "Sample report generated"
    else
        print_error "API connection failed"
        print_info "Check your credentials and try again"
        exit 1
    fi
    
    cd ../..
}

# Install skills
install_skills() {
    print_header "Step 4: Installing Skills"
    
    print_info "Enabling meal-to-intervals..."
    openclaw skills enable meal-to-intervals 2>/dev/null || print_warning "May need manual enable"
    
    print_info "Enabling intervals-status-reporter..."
    openclaw skills enable intervals-status-reporter 2>/dev/null || print_warning "May need manual enable"
    
    print_success "Skills installed"
}

# Show completion
show_completion() {
    print_header "🎉 Installation Complete!"
    
    print_success "Body Management System is ready!"
    echo ""
    print_info "📦 GitHub: https://github.com/leozvc/body-management-system"
    print_info "📚 Docs: See INSTALL.md and USAGE_PROMPTS.md"
    echo ""
    print_info "🚀 Quick Start:"
    print_info '  In OpenClaw chat, send: "查看我今天的身体状态"'
    echo ""
    print_info "📝 Common Commands:"
    print_info '  • "早餐吃了 XXX，记录一下" - Log a meal'
    print_info '  • "我今天适合打网球吗" - Training decision'
    print_info '  • openclaw skills list - List skills'
    echo ""
    print_warning "Next: Read USAGE_PROMPTS.md for example conversations!"
}

# Main
main() {
    print_header "🏋️ Body Management System - One-Click Installer"
    print_info "GitHub: https://github.com/leozvc/body-management-system"
    echo ""
    
    check_prerequisites
    clone_repo
    setup_config
    test_connection
    install_skills
    show_completion
}

main "$@"
