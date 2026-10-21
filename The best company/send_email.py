import smtplib, ssl
import os

def send_email(user_email, topic, message):
    host = "smtp.gmail.com"
    port = 465

    username = "fatemeehgorjiii@gmail.com"
    password = os.getenv("PASSWORD")

    receiver_email = "fatemeehgorjiii@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print("Connected to Gmail!")

        server.login(username, password)
        print("Login successful!")

        email_message = f"""Subject: New email from {user_email}

        From: {user_email}
        Topic: {topic}

        {message}
        """

        server.sendmail(username, receiver_email, email_message.encode("utf-8"))
        print("Email sent successfully!")