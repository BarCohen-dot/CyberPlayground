# Google Dorking & OSINT Cheatsheet — CyberPlayground

This cheatsheet outlines powerful Google search operators (aka "Google Dorks") for ethical hacking, digital footprint reconnaissance, and open-source intelligence (OSINT).

> WARNING: Use these queries **only for educational purposes** and on **authorized environments**. Exploiting or scanning without consent is illegal.

```
# LEAK DETECTION & PASSWORD EXPOSURE
site:pastebin.com "Microsoft" "password" OR "credentials"
"Microsoft data breach" OR "cyber incident details" filetype:pdf OR filetype:xlsx

# PUBLIC CLOUD FILE DISCOVERY
site:drive.google.com "Microsoft" OR "cybersecurity" filetype:doc OR filetype:csv
site:onedrive.live.com "Microsoft confidential" filetype:pdf OR filetype:csv
site:storage.googleapis.com "microsoft" filetype:csv OR filetype:json
site:s3.amazonaws.com "microsoft" filetype:csv OR filetype:json

# SECURITY & INCIDENT REPORTS
"Microsoft SOC report" OR "SOC logs" filetype:pdf OR filetype:csv
site:microsoft.com "cybersecurity report" OR "incident analysis" filetype:pdf OR filetype:xlsx

# CONFIGURATION FILES & SECRETS
site:microsoft.com filetype:config OR filetype:ini "password" OR "key"
site:api.microsoft.com "key=" OR "token=" OR "secret="
filetype:txt OR filetype:log "password=" OR "pwd="

# LOGIN PANELS & ADMIN INTERFACES
intitle:"Microsoft" inurl:"/admin" OR inurl:"/login"
site:microsoft.com intitle:"index of /" OR "parent directory"

# NETWORK & LOG LEAKS
filetype:conf OR filetype:cfg "interface" OR "network"
filetype:log "HTTP/1.1 200 OK" OR "GET /"
site:microsoft.com filetype:log "password" OR "user"

# WEB SERVER / SOFTWARE VERSION DISCLOSURE
intitle:"Index of /" "Apache/2.4" OR "nginx/1.18"

# DATABASE & SQL PANELS
inurl:"phpmyadmin/" "Welcome to phpMyAdmin" OR "MySQL server"

# DOCUMENTS MARKED CONFIDENTIAL
site:microsoft.com intitle:"confidential" OR "internal use only" filetype:pdf OR filetype:docx

# COMPANY DOMAIN INTEL
site:microsoft.com filetype:csv OR filetype:xlsx "cyber attack" OR "incident logs"

# SOURCE CODE SECRETS
site:github.com "password" OR "apikey" filename:env
```

## Recommended Tools for OSINT Expansion

* **theHarvester** — Collects emails, subdomains, hosts, employee names.
* **Spiderfoot** — Automates OSINT across dozens of data sources.
* **FOCA** — Extracts metadata and hidden info from public documents.
* **Metagoofil** — Finds company documents and extracts useful metadata.

## Suggested Additions

* Create a Google Dork automation script with Python (`requests`, `BeautifulSoup`, `Selenium`)
* Integrate with Shodan/Censys API for exposed services
* Add filtering logic for result parsing and notification (e.g., Slack or email alerts)

---

Author: Bar Cohen
