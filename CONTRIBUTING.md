# Contributing to Body Management System

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

---

## 🌟 How Can I Contribute?

### Types of Contributions

#### 1. Reporting Bugs 🐛
- Use GitHub Issues to report bugs
- Provide clear reproduction steps
- Include error messages and system information
- See [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)

#### 2. Suggesting Features ✨
- Open an Issue with `enhancement` label
- Describe the problem or opportunity
- Explain why this feature would be useful
- See [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md)

#### 3. Submitting Code 🔧
- Fork the repository
- Create a feature branch
- Make changes following coding standards
- Submit a Pull Request

#### 4. Improving Documentation 📚
- Fix typos or unclear instructions
- Add examples or tutorials
- Update API documentation
- Translate docs to other languages

#### 5. Testing ✅
- Write unit tests for new features
- Test existing functionality
- Report edge cases that fail
- Help achieve test coverage goals

---

## 🚀 Quick Start for Contributors

### 1. Fork and Clone

```bash
# Fork on GitHub, then clone locally
git clone https://github.com/YOUR_USERNAME/body-management-system.git
cd body-management-system
```

### 2. Set Up Development Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Optional: Set up pre-commit hooks
pre-commit install
```

### 3. Create a Branch

```bash
# Create a feature branch (use descriptive name)
git checkout -b feature/add-meal-photo-analysis

# Or fix a bug
git checkout -b fix/config-validation-error
```

---

## 💻 Coding Standards

### Python Style Guide

We follow **[PEP 8](https://pep8.org/)** with some additions:

- **Line length:** Max 88 characters (Black compatible)
- **Imports:** Grouped and sorted alphabetically
- **Functions:** Clear docstrings for all public functions
- **Type hints:** Use for all function parameters and return values
- **Error handling:** Descriptive exceptions with context

### Example Code Style

```python
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

def fetch_meal_data(meal_name: str, max_retries: int = 3) -> Optional[Dict[str, Any]]:
    """Fetch nutrition data for a meal from OpenFoodFacts API.
    
    Args:
        meal_name: Name of the meal to look up
        max_retries: Number of times to retry on failure
        
    Returns:
        Dictionary with nutritional information, or None if not found
        
    Raises:
        ApiError: If API call fails after all retries
    """
    for attempt in range(max_retries):
        try:
            response = api_call(f"/search?search_terms={meal_name}")
            if response.status_code == 200:
                return parse_response(response.json())
            
            logger.warning(f"Attempt {attempt + 1} failed")
            
        except NetworkError as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # Exponential backoff