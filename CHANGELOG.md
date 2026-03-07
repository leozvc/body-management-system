# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-03-08

### Added
- **Config Schema Validation** - Validates API key format before making API calls
- **Enhanced Error Handling** - Descriptive error messages with troubleshooting steps
- **Retry Logic** - Automatic retries for transient network failures (exponential backoff)
- **Structured Logging** - Timestamped logs with log levels (INFO, WARNING, ERROR)
- **`.env.example` Support** - Environment-based credential management guide
- **Comprehensive .gitignore** - Enhanced protection for data directories across all skill folders

### Changed
- **Updated README links** - Fixed broken references to non-existent documentation
- **Dependency version pinning** - All Python dependencies now pinned to exact versions
- **Improved data isolation** - Clearer separation between code and user data
- **Better error messages** - Users now get actionable guidance when issues occur

### Security
- **Removed sensitive config from repo** - Only `config_template.json` remains in repository
- **Added explicit `.gitignore` rules** in each skill directory for extra protection
- **Config validation** - Prevents invalid API keys from causing confusing errors

### Documentation
- **Created CHANGELOG.md** - Tracks all version changes going forward
- **Updated INSTALL.md** - Clarified data storage location and backup procedures
- **Added CODE_REVIEW_v1.0.0.md** - Public code review for transparency

### Internal
- **Bumped VERSION** to 1.1.0
- **Standardized requirements.txt** - All dependencies now use exact version pins
- **Refactored error handling patterns** - Consistent try/catch/raise throughout codebase

---

## [1.0.0] - 2026-03-06

### Initial Release

#### Features
- ✅ **meal-to-intervals** skill - Auto-log meals to intervals.icu with calculated macros
- ✅ **intervals-status-reporter** skill - Generate standardized body status reports
- ✅ One-click installation via `setup.sh`
- ✅ Interactive OpenClaw chat installation
- ✅ Privacy-first architecture - User data stored separately from code
- ✅ Comprehensive documentation:
  - README.md (quick start)
  - INSTALL.md (detailed install guide)
  - USAGE_PROMPTS.md (prompt library)
  - DATA_STORAGE.md (data management best practices)

#### Configuration
- intervals.icu API integration
- Athlete ID support
- Wellness field mapping

#### Limitations
- Single platform support (intervals.icu only)
- No meal photo analysis
- Manual data entry required

---

## [Unreleased]

### Planned for v1.2.0
- GitHub Actions CI/CD pipeline
- Automated testing framework
- Type hints throughout codebase
- CONTRIBUTING.md for contributors
- ISSUE templates for bug reporting

### Planned for v1.3.0
- Meal photo analysis (OCR-based nutrition estimation)
- Multi-platform sync (Strava, Garmin Connect)
- CSV/PDF export functionality
- Web dashboard for health visualization
