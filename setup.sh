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

# Clone or update repository
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

# Copy skills from workspace if they exist
copy_skills() {
    print_header "Step 2: Setting Up Skills"
    
    WORKSPACE_SKILLS="$HOME/.openclaw/workspace/skills"
    
    # meal-to-intervals
    if [ -d "$WORKSPACE_SKILLS/meal-to-intervals" ]; then
        print_success "meal-to-intervals already installed"
    else
        print_info "meal-to-intervals not found, skipping..."
    fi
    
    # intervals-status-reporter
    if [ -d "$WORKSPACE_SKILLS/intervals-status-reporter" ]; then
        print_success "intervals-status-reporter already installed"
    else
        print_info "intervals-status-reporter not found, skipping..."
    fi
}

# Run interactive installer
run_installer() {
    print_header "Step 3: Running Interactive Setup"
    
    cd "$PROJECT_DIR"
    
    if [ -f "install.sh" ]; then
        print_info "Starting interactive setup..."
        print_warning "You'll need your intervals.icu API credentials ready"
        print_info "Get API Key: https://intervals.icu → Settings → API"
        echo ""
        
        ./install.sh
    else
        print_error "install.sh not found!"
        exit 1
    fi
}

# Show completion
show_completion() {
    print_header "🎉 Installation Complete!"
    
    print_success "Body Management System is ready!"
    echo ""
    print_info "📦 GitHub: https://github.com/leozvc/body-management-system"
    print_info "📚 Docs: $PROJECT_DIR/README.md"
    echo ""
    print_info "🚀 Quick Start:"
    print_info '  In OpenClaw chat, send: "查看我今天的身体状态"'
    echo ""
    print_info "📝 Common Commands:"
    print_info '  • "早餐吃了 XXX，记录一下" - Log a meal'
    print_info '  • "我今天适合打网球吗" - Training decision'
    print_info '  • openclaw skills list - List installed skills'
    echo ""
}

# Main
main() {
    print_header "🏋️ Body Management System - One-Click Installer"
    print_info "GitHub: https://github.com/leozvc/body-management-system"
    echo ""
    
    check_prerequisites
    clone_repo
    copy_skills
    run_installer
    show_completion
}

main "$@"
