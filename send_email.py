import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "fatemeehgorjiii@gmail.com"
    password = "bzcc oglh enze ijce"

    receiver_email = "fatemeehgorjiii@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print("Connected to Gmail!")

        server.login(username, password)
        print("Login successful!")

        server.sendmail(username, receiver_email, message)
        print("Email sent successfully!")