import smtplib
import ssl
import os

# email standard library which creates email client session
# used to write scripts to send emails
# needs parameters: host, port

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'florin.mihalcioiu27@gmail.com'
    password = os.getenv("PASSWORD") #I give a name to my environment variable
    # getenv() acces the os and get the password from env variable
    # the password is stored on the env variable in the os

    receiver = 'florin.mihalcioiu27@gmail.com'
    context = ssl.create_default_context()
    # \ for taking the Subject as Title of the email

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    # SMTP = Simple Mail Transfer Protocol -> used to send and receive email
    # SSL = Secure Socket Layer -> establish an encrypted link between a server and the client
    # password = 'wqiezwoxzndjvasr'
