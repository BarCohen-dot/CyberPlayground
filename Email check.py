import re              # לשימוש בביטויים רגולריים למציאת קישורים ומילים חשודות
import urllib.parse    # לפענוח כתובות URL ובדיקת דומיינים חשודים

# נגדיר רשימת מילים שמעידות על פישינג
PHISHING_KEYWORDS = [
    "urgent", "danger", "your account will be locked", "click here immediately", "mandatory verification",
    "enter credit card details", "password reset required", "verify your identity", "unusual activity detected",
    "confirm your information", "your account has been compromised", "secure your account now",
    "update your payment method", "free gift", "win a prize", "limited-time offer", "claim your reward",
    "suspicious login attempt", "your invoice is ready", "your PayPal account needs verification"
]

# נגדיר רשימת דומיינים חשודים לדוגמה
SUSPICIOUS_DOMAINS = [
    "bit.ly", "tinyurl.com", "free-gift.com", "verify-now.com", "secure-login.com", "account-security.com",
    "banking-alert.com", "paypal-support.com", "appleid-verify.com", "amazon-secure.com",
    "update-billing.com", "claim-reward.net", "freevoucher.com", "lottery-winner.com", "security-check.com"
]

def extract_links(text):
    """פונקציה שמוצאת את כל הקישורים במייל"""
    urls = re.findall(r'https?://\S+', text)
    parsed_urls = [urllib.parse.urlparse(url).netloc for url in urls]
    return parsed_urls

def check_suspicious_links(links):
    """פונקציה שבודקת אם יש קישורים חשודים"""
    return [link for link in links if any(domain in link for domain in SUSPICIOUS_DOMAINS)]


def check_phishing_words(text):
    """פונקציה שבודקת אם יש מילים שמעידות על פישינג"""
    found_words = [word for word in PHISHING_KEYWORDS if word in text]
    return found_words


def analyze_email(email_text):
    """פונקצית הפעלה לניתוח והחזרת ציון חשד"""
    links = extract_links(email_text)
    suspicious_links = check_suspicious_links(links)
    phishing_words = check_phishing_words(email_text)

    score = len(suspicious_links) * 2 + len(phishing_words)  # כל קישור חשוד מוסיף 2 נק',בעוד שכל מילה חשודה מוסיפה נקודה
    Result = {
        "total_score": score,
        "suspicious_links": suspicious_links,
        "phishing_words": phishing_words,
             }
    return Result

# ---------------------------------------------------------------- Main ------------------------------------------------
if __name__ == "__main__":
    with open("email_example.rtf", "r", encoding="utf-8") as file:
        email_content = file.read()

    result = analyze_email(email_content)
    print("\nEmail Analysis:")
    print(f"Total Suspicion Score: {result['total_score']}")
    print(f"Suspicious Links: {result['suspicious_links']}")
    print(f"Phishing Words: {result['phishing_words']}")
