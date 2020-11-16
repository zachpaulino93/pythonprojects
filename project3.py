#!/usr/bin/env python3

from email.message import EmailMessage
import getpass
import smtplib
import mimetypes
import os.path

def load_smtp():
    sender = 'some email'
    print("connecting to smtp server will")
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail_pass = getpass.getpass('Password? ')
    print(mail_pass)
    mail_server.login(sender, mail_pass)
    print("login sucessful")
    return sender

def create_email(sender):
    # sender = "zachpaulino93@gmail.com"
    recipient = "some email"
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


















if __name__ == "__main__":
    print("Starting program, will initiate load_smtp")
    sender = load_smtp()
    print("gathering email data to complie")
    email = create_email(sender)
    print("sending email")
