# Semgrep PoC

## What This Shows
- Local Semgrep scanning with **community and custom rules**  
- CI/CD integration (**GitHub Actions** ) 
- **SARIF upload** to GitHub Code Scanning  


---

## Quickstart

### Local Scan
```bash
# Install Semgrep
pip install semgrep
```
# Run a local scan with security-audit rules
semgrep --config p/security-audit .
CI/CD Integration
GitHub Actions: .github/workflows/semgrep.yml


Custom Rules
Example custom rule:

```bash
semgrep-rules/no-sqli.yaml
```
Final Repo Layout 
```perl
semgrep-demo/
├── app/
│   └── app.py             # Main application code
├── tests/
│   └── test_app.py        # Unit tests
├── semgrep-rules/
│   └── no-sqli.yaml       # Custom security rule example
├── requirements.txt
├── .semgrepignore
├── .github/
│   └── workflows/
│       └── semgrep.yml    # GitHub Actions workflow
└── README.md

```
Summary
- Once you push this repo to GitHub, you get:

- Local scans for quick feedback

- CI enforcement to catch issues during PRs


This PoC demonstrates how to integrate Semgrep in both local and CI/CD workflows, including custom security rules.

