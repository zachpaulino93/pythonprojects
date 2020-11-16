#!/usr/bin/env python3

from email.message import EmailMessage
import getpass
import smtplib
import mimetypes
import os.path

def load_smtp()
    sender = "zachpaulino93@gmail.com"
    print("connecting to smtp server will")
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server = getpass.getpass('Password? ')
    mail_server.login(sender, getpass)
    print("login sucessful")
    return sender

def create_email(sender)
    # sender = "zachpaulino93@gmail.com"
    recipient = "mallorie98@gmail.com"
    # setting to and from portion
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
    sender = load_smtp()
    email = create_email(sender)
