## A record of bugs found, investigated and fixed during development

| ID | Date | Description | Root Cause | Fix | Status |
|---|-----|--------------|------------|-----|-------|
| 1 | 2025-06-28 |`is_allowed_file failed for trailing spaces`| Trailing spaces stayed in extension when using os.path.splitext | Strip filename before splitext | `Fixed`