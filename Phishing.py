"""
אתרים כמו Guerrilla Mail או Mailinator מספקים כתובת דוא"ל זמנית ומסתירה את פרטי השולח.

"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# הגדרת פרטי השולח המזויף
sender_email = "anonymous@example.com"  # כתובת דוא"ל מזויפת
recipient_email = "victim@example.com"  # כתובת הנמען
subject = "החשבון שלך דורש עדכון"
body = """
שלום,

אנו שמים לב שישנה בעיה בחשבון שלך. כדי לשמור על אבטחת החשבון, עליך לעדכן את פרטי החשבון שלך מיידית. 
לחץ על הקישור הבא כדי לעדכן את החשבון שלך:

http://example.com/fake-login-page

בברכה,
צוות התמיכה
"""

message = MIMEMultipart()
message['From'] = sender_email  # אימייל מוצפן
message['To'] = recipient_email # אימייל יעד
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# יצירת חיבור לשרת SMTP
try:
    server = smtplib.SMTP('smtp.mailtrap.io', 587)  # דוגמה לשימוש ב-Mailtrap (שרת SMTP חיצוני)
    server.starttls()  # הפעלת הצפנה
    server.login("your_username", "your_password")  # כניסה עם פרטי השרת (אם נדרש)
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)  # שליחת ההודעה
    server.quit()
    print("ההודעה נשלחה בהצלחה!")
except Exception as e:
    print(f"לא הצלחנו לשלוח את ההודעה: {e}")

