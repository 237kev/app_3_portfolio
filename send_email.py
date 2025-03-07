import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    password = 'sbzv bboj uhvh ynlh'  # not recommended
    user_name = 'emlyssaker@gmail.com'
    context = ssl.create_default_context()

    receiver = 'emlyssaker@gmail.com'
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
