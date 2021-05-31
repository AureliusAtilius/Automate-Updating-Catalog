#!/usr/bin/env python3
from re import sub
import shutil
import psutil
import emails
import os
import email.message

def health_check():
        # Collect system data
        cpu_usage= psutil.cpu_percent()
        total, used, free = shutil.disk_usage("/")
        disk_space = ((used/total)*100)
        mem = ((psutil.virtual_memory().available)/1000000)
        loopback = psutil.net_if_addrs()["lo"][0][1]
        
        # Collect error email information
        sender = 'automation@example.com'
        recipient= "{}@example.com".format(os.environ.get('USER'))          
        body = 'Please check your system and resolve the issue as soon as possible'
        subject = ""

        # Define conditions for each error and provide appropriate subject line message.
        if cpu_usage>80:
                subject += 'Error - CPU usage is over 80%'
        if disk_space<20:
                subject += 'Error - Available disk space is less than 20%'
        if mem<500:
                subject +='Error - Available memory is less than 500MB'
        
        if loopback!="127.0.0.1":
                subject += 'Error - localhost cannot be resolved to 127.0.0.1'
        
        if subject!="":
                error_email(sender, recipient, body, subject)
                

def error_email(sender, recipient, subject, body):
        # Basic Email formatting for error email.
        message = email.message.EmailMessage()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)

        # Send error email
        emails.send(message)


if __name__=="__main__":
        
        health_check()