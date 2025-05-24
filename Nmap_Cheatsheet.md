# 📡 Nmap Cheatsheet — CyberPlayground

This file contains commonly used **Nmap commands** for network scanning, host discovery, and vulnerability enumeration.

> ⚠️ For **ethical use only** in authorized environments.

---

1. sudo nmap -sS -p 1-65535 10.0.0.0/24
   - TCP SYN scan on all 65,535 ports in the subnet.
   - Stealthy scan that does not complete connections.

2. sudo nmap -sU -p 1-65535 10.0.0.0/24
   - UDP scan across all ports to detect services like DNS, DHCP.

3. sudo nmap -A 10.0.0.0/24
   - Aggressive scan: detects OS, versions, runs scripts & traceroute.

4. sudo nmap -sV 10.0.0.0/24
   - Version detection on open ports.

5. sudo nmap -O 10.0.0.0/24
   - Operating system detection.

6. sudo nmap -sT -p 1-65535 10.0.0.0/24
   - Full TCP connect scan (less stealthy, more reliable).

7. sudo nmap -p 53 --script=dns-zone-transfer example.com
   - Tests for misconfigured DNS zone transfer on example.com.

8. Host Discovery Examples:
   sudo nmap -sn 10.0.0.0/24
   sudo nmap -p 80 10.0.0.0/24
   sudo nmap -sn -Pn 10.0.0.0/24
   sudo nmap -sn 10.10.40.254/24
   sudo nmap -p- 10.10.40.254
   - Performs ping scans to detect live hosts.

9. sudo nmap -sF -p 1-65535 10.0.0.0/24
   - TCP FIN scan — stealthy way to identify open ports.

10. sudo nmap -sN -p 1-65535 10.0.0.0/24
    - TCP NULL scan — sends packets with no flags for OS-specific behavior.

11. nmap -sS 192.168.1.0/24
    - Basic SYN scan on a local subnet.
