#!/usr/bin/env python3

from email.message import EmailMessage
import getpass
import smtplib
import mimetypes
import os.path


def setup_users():
    user = input("Please enter your email ")
    print(f" this will be the senders email {user}")
    recipient = input("Please input senders ")
    print(f"this will be the recipients email {recipient}")
    return user, recipient


def load_smtp(sender, message):
    user = input("input desired email to send from ")
    print("connecting to smtp server will")
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail_pass = getpass.getpass('Password? ')
    print(mail_pass)
    mail_server.login(sender, mail_pass)
    print("login sucessful")
    mail_server.send_message(message)
    print("email sent")
    mail_server.quit()

def create_email(user, recipient):
    sender = user
    recipient = recipient
    # setting to and from portion
    message = EmailMessage()
    message["From"] = sender
    message["to"] = recipient
    # setting up subject field
    message["Subject"] = f"Greetings this is from {sender} to {recipient}"
    body = """ Hey this is my first pythonic email program lets see how this works
    out! """
    # setting variable and putting body into a function
    message.set_content(body)
    return message

def get_file()
    attachment_path = /"whatever_path.png"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_subtype.split('/', 1)
    with open(attachment_path, 'rb') as ap:
        maintype=mime_type,
        subtype=mime_subtype,
        filename=os.path.basename(attachment_path)

   return ap


if __name__ == "__main__":
    user, recipient = setup_users()
    email = create_email(user, recipient)
    print("gathering email data to complie")
    print("Starting program, will initiate load_smtp")
    smtp_server = load_smtp(email)
    print("sending email")
