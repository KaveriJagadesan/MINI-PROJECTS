import smtplib
from email.mime.text import MIMEText

# ---------- STORED ATM PIN ----------
stored_pin = "123456"  # Example stored PIN

# ---------- EMAIL ALERT FUNCTION ----------
def send_alert_email():
    sender_email = "your_email@gmail.com"       # your email
    sender_password = "your_app_password"       # Gmail App Password
    receiver_email = "receiver_email@gmail.com" # who should receive alert

    subject = "ATM Alert: Wrong PIN Entered 3 Times"
    body = "Warning! Someone entered the wrong ATM PIN three times."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Alert email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


# ---------- PIN VALIDATION ----------
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your ATM PIN: ")

    if entered_pin == stored_pin:
        print("PIN correct. Access granted.")
        break
    else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {3 - attempts}")

# If user fails 3 times → send email alert
if attempts == 3:
    print("PIN blocked! Sending security alert email...")
    send_alert_email()
    print("Your ATM PIN has been blocked due to multiple incorrect attempts.")