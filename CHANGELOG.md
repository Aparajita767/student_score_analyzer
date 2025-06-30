
---

##  **`CHANGELOG.md`**

```markdown
# 📋 CHANGELOG

All notable changes to this project will be documented here.

This project follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]
- Add frontend UI
- Improve test coverage

## [0.1.1] - 2025-06-28
### Fixed
- `is_allowed_file` now strips trailing spaces to handle filenames like `'grades.csv '` correctly.

## [0.1.0] - 2025-06-27
### Added
- Basic FastAPI app with `/upload` route
- Validates `.csv` file uploads only
- Unit tests for `is_allowed_file`
- TestClient tests for `/upload` route
- BUG_LOG.md for bug tracking
- README.md for project overview
