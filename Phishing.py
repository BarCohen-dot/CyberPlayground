"""
Phishing Email Simulation Script

This Python script simulates the sending of a phishing-style email for cybersecurity awareness
and educational testing purposes only. It demonstrates how threat actors might attempt to
send deceptive emails using fake sender identities and suspicious links.

🚫 Disclaimer: This script must not be used for any unauthorized or malicious activities.
It is intended strictly for learning and ethical hacking practices within controlled environments.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define fake sender and recipient details
sender_email = "anonymous@example.com"       # Spoofed sender email address
recipient_email = "victim@example.com"       # Recipient's email address
subject = "Your Account Requires Immediate Action"
body = """
Hello,

We've noticed an issue with your account. To maintain account security, you must immediately update your account information.
Please click the link below to verify and secure your account:

http://example.com/fake-login-page

Sincerely,
Support Team
"""

# Construct the email message
message = MIMEMultipart()
message['From'] = sender_email        # Set the spoofed sender
message['To'] = recipient_email       # Set the recipient
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Attempt to connect to an SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.mailtrap.io', 587)  # Using Mailtrap SMTP for testing
    server.starttls()                               # Enable encryption
    server.login("your_username", "your_password")  # Replace with your Mailtrap credentials
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)  # Send the message
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
