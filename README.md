# CyberPlayground - Vulnerability & Attack Simulation Toolkit ☠️

Welcome to **CyberPlayground**, an advanced multi-tool cybersecurity repository developed for educational and ethical testing purposes.
This project contains a collection of Python-based scripts designed to scan, simulate, and test modern web application vulnerabilities such as XSS, SQLi, Command Injection, SSTI, and more.

> 🚨 **DISCLAIMER**: This toolkit is for educational purposes only. Do not use it against systems without explicit authorization. Unauthorized testing is illegal and unethical.

---

## Repository Structure

```bash
CyberPlayground/
├── Bypass Injection Tool.py      # Tests login bypass via hash-based or logical SQL payloads
├── DDOS.py                      # Simple simulation of DDoS traffic
├── Email_check.py              # Analyzes email contents for phishing indicators
├── Phishing_send.py            # Simulates sending of a phishing email
├── SQL_Injection.py            # Scanner for classic SQLi payloads
├── XSS_scanner.py              # Quick test for reflected XSS via URL parameters
├── Vulnerability_Scanner.py    # Advanced scanner for XSS, CMDi, LFI, SSTI, POST, header & cookie injections
├── LICENSE                     # MIT License
```

---

## Core Tools Overview

### `Bypass Injection Tool`

Tests login forms for bypass using payloads such as:

* `' OR '1'='1`
* `' AND 1=0 UNION SELECT ...`
* Hash injection using `md5()` and `sha1()`

### `DDOS.py`

Simulates basic denial-of-service attacks by sending rapid repeated requests.

### `Email_check.py`

Scans `.rtf` or `.txt` emails for:

* Suspicious URLs
* Phishing trigger words (e.g., "Verify your account", "Click here immediately")

### `Phishing_send.py`

Sends a fake phishing-style email (via SMTP) for internal awareness simulations.

### `SQL_Injection.py`

Injects a variety of SQLi payloads:

* Boolean-based
* Error-based
* Union-based
* Bypass authentication

### `XSS_scanner.py`

Tests a list of reflected XSS payloads in a query parameter. Includes:

* `<script>` tags
* `<img onerror>`
* SVG payloads

### `Vulnerability_Scanner.py` 

**The most advanced module**:

* XSS (GET/POST/Header/Cookie)
* Command injection (time-based & reflected)
* LFI (Local File Inclusion)
* SSTI (Server-Side Template Injection)
* Custom header/cookie payload injection
* Time-delay detection (blind CMDi)
* Status code anomaly checks

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/BarCohen-dot/CyberPlayground.git
cd CyberPlayground
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Run a scanner (example: XSS)

```bash
python XSS_scanner.py
```

Edit the target URL inside the script before running:

```python
target_url = "http://example.com/search"
```

---

## Permissions & Legal

This project is released under the [MIT License](./LICENSE).

* You may use, modify, and distribute this project.
* You may **not** use it for illegal penetration testing.

If you are an instructor or security trainer, feel free to adapt this project for CTFs or labs with attribution.

---

## Author

Built with passion and curiosity by:
**Bar Cohen**

> Connect on [LinkedIn](https://www.linkedin.com/in/bar--cohen-)
