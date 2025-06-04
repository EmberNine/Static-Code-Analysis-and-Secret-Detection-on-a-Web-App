# Secure Flask App with Static Analysis

This is a deliberately vulnerable Python Flask app used to demonstrate static code analysis and secret detection in a CI/CD pipeline.

## Tools Used

- Bandit: Static analyzer for Python
- Semgrep: Lightweight and customizable SAST
- Gitleaks: Secret detection in source history and files
- GitHub Actions: CI pipeline

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## CI/CD Security Checks

On every push or PR to `main`, GitHub Actions will:
- Run Bandit on the source code
- Run Semgrep with default or custom rules
- Detect secrets using Gitleaks

## Try it

```bash
curl "http://localhost:5000/vuln?input=__import__('os').system('ls')"
```

!!!!!!!!!!!!!This is insecure and used only for demonstration.!!!!!!!!!!!!!!!!!!!!!!!!!!!
