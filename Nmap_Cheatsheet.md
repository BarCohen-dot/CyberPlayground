# Nmap Cheatsheet — CyberPlayground

This cheatsheet contains essential `nmap` commands for scanning, enumeration, and vulnerability assessment.

> ⚠️ For **educational and authorized use** only. Do **not** scan networks without permission.

---

```bash
# Basic Scanning

sudo nmap -sS -p 1-65535 10.0.0.0/24          # Stealth SYN scan on all ports
sudo nmap -sT -p 1-65535 10.0.0.0/24          # Full TCP connect scan (reliable, less stealthy)
sudo nmap -sU -p 1-65535 10.0.0.0/24          # UDP scan on all ports

sudo nmap -p- 192.168.1.1                     # Scan all ports on a single host
sudo nmap -F 192.168.1.1                      # Fast scan (default top 100 ports)

# Advanced Enumeration

sudo nmap -A 10.0.0.0/24                      # Aggressive scan (OS, services, scripts, traceroute)
sudo nmap -sV 10.0.0.0/24                     # Service version detection
sudo nmap -O 10.0.0.0/24                      # OS detection
sudo nmap --top-ports 100 10.0.0.0/24         # Scan top 100 most common ports
sudo nmap -T4 -sS 10.0.0.0/24                 # Faster execution with timing template (T0–T5)

# Host Discovery

sudo nmap -sn 10.0.0.0/24                     # Ping scan (host discovery)
sudo nmap -Pn 10.0.0.0/24                     # Treat all hosts as online (skip ping)
sudo nmap -sn -n 192.168.1.0/24               # Discovery without DNS resolution

# Vulnerability Scanning (Scripts)

sudo nmap --script vuln 192.168.1.1           # Run vulnerability detection scripts
sudo nmap --script default 192.168.1.1        # Run default scripts
sudo nmap --script safe 192.168.1.1           # Non-intrusive checks only
sudo nmap -sV --script=http-vuln* 192.168.1.1 # HTTP-related vulnerabilities
sudo nmap --script smb-vuln* 192.168.1.1      # SMB-related vulnerabilities

# Web & DNS Enumeration

sudo nmap -p 80,443 --script http-enum 192.168.1.1   # Web directory brute-forcing
sudo nmap --script dns-zone-transfer -p 53 example.com  # Attempt zone transfer
sudo nmap --script dns-brute example.com            # Subdomain brute-forcing

# Firewall Evasion & Stealth

sudo nmap -sS -T2 -f 10.0.0.0/24                     # Fragmented packets (IDS evasion)
sudo nmap -sS --data-length 200 10.0.0.0/24          # Add padding to packets
sudo nmap --source-port 53 10.0.0.0/24               # Spoof source port (e.g. DNS)
sudo nmap -D RND:10 192.168.1.1                      # Decoy scan with 10 fake sources
sudo nmap -S 192.168.1.100 192.168.1.1                # Spoof source IP

# NSE (Nmap Scripting Engine) Examples

sudo nmap --script ftp-anon,ftp-bounce 192.168.1.1   # FTP scan
sudo nmap --script ssh2-enum-algos 192.168.1.1       # SSH algorithms
sudo nmap --script ssl-cert,ssl-enum-ciphers 192.168.1.1  # SSL info
sudo nmap --script smb-os-discovery 192.168.1.1      # SMB OS details

# Output Formats

sudo nmap -oN scan.txt 192.168.1.1                   # Normal output
sudo nmap -oX scan.xml 192.168.1.1                   # XML output
sudo nmap -oG scan.gnmap 192.168.1.1                 # Greppable output
sudo nmap -oA full-scan 192.168.1.1                  # All formats combined

# Misc & Quick Tips

nmap -v                                               # Verbose mode
nmap -6 2606:4700::6810:1348                          # IPv6 scan
nmap --reason 192.168.1.1                             # Show why host is up
nmap --script-help vuln                               # Show info on vulnerability scripts

```
