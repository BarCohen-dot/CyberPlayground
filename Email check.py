"""
Email Phishing Analyzer 🛡️
---------------------------

This script is designed to analyze the content of email messages and detect potential phishing attempts.
It scans for:
- Suspicious **keywords** commonly used in phishing emails (e.g., "urgent", "click here", "verify account").
- **URLs** pointing to known suspicious or shortened domains (e.g., "bit.ly", "secure-login.com").

How it works:
-------------
1. Reads the contents of an email file (`email_example.rtf`).
2. Extracts all URLs and checks if any belong to a suspicious domain.
3. Searches for phishing-related keywords in the text.
4. Calculates a total **suspicion score**:
   - +2 points per suspicious link.
   - +1 point per phishing keyword.

The script outputs the total score and the exact links/keywords detected.

Author: Bar Cohen
"""

import re                # For using regular expressions to find links and suspicious words
import urllib.parse      # For parsing and analyzing URL domains

# Define a list of keywords typically associated with phishing
PHISHING_KEYWORDS = [
    "urgent", "danger", "your account will be locked", "click here immediately", "mandatory verification",
    "enter credit card details", "password reset required", "verify your identity", "unusual activity detected",
    "confirm your information", "your account has been compromised", "secure your account now",
    "update your payment method", "free gift", "win a prize", "limited-time offer", "claim your reward",
    "suspicious login attempt", "your invoice is ready", "your PayPal account needs verification"
]

# Define a list of suspicious domains (commonly used in phishing)
SUSPICIOUS_DOMAINS = [
    "bit.ly", "tinyurl.com", "free-gift.com", "verify-now.com", "secure-login.com", "account-security.com",
    "banking-alert.com", "paypal-support.com", "appleid-verify.com", "amazon-secure.com",
    "update-billing.com", "claim-reward.net", "freevoucher.com", "lottery-winner.com", "security-check.com"
]

def extract_links(text):
    """Extract all URLs from the given text."""
    urls = re.findall(r'https?://\S+', text)
    parsed_urls = [urllib.parse.urlparse(url).netloc for url in urls]
    return parsed_urls

def check_suspicious_links(links):
    """Check whether any of the links point to suspicious domains."""
    return [link for link in links if any(domain in link for domain in SUSPICIOUS_DOMAINS)]

def check_phishing_words(text):
    """Check whether the text contains known phishing keywords."""
    found_words = [word for word in PHISHING_KEYWORDS if word in text]
    return found_words

def analyze_email(email_text):
    """Analyze the email and return a suspicion score with details."""
    links = extract_links(email_text)
    suspicious_links = check_suspicious_links(links)
    phishing_words = check_phishing_words(email_text)

    # Each suspicious link adds 2 points, each keyword adds 1 point
    score = len(suspicious_links) * 2 + len(phishing_words)
    result = {
        "total_score": score,
        "suspicious_links": suspicious_links,
        "phishing_words": phishing_words,
    }
    return result

# ------------------------------- Main Execution --------------------------------
if __name__ == "__main__":
    with open("email_example.rtf", "r", encoding="utf-8") as file:
        email_content = file.read()

    result = analyze_email(email_content)
    print("\nEmail Analysis:")
    print(f"Total Suspicion Score: {result['total_score']}")
    print(f"Suspicious Links: {result['suspicious_links']}")
    print(f"Phishing Words: {result['phishing_words']}")
