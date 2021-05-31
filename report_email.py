#!/usr/bin/env python3

from reportlab.platypus import paragraph
import os
import reports
import run
import emails
from datetime import date


def  processReport():
        pdf_lines=[]
        for file in os.listdir("/home/{}//supplier-data/descriptions/".format(os.environ.get('USER'))):
                # Process file contents
                data=run.processDescription(file)
                
                # Collect name and data for each file, separate with empty line
                name = "name: {}".format(data["name"])
                weight = "weight: {}".format(data["weight"])
                empty_line= "<br/>"
                pdf_lines.extend([name, weight,empty_line])
        # Join line contents with a new line
        pdf_data="<br/>".join(pdf_lines)        
        return pdf_data

if __name__=="__main__":
        
        # Collect todays date and put it in the report title
        today = date.today()
        title= "Processed Update on {}".format(today.strftime("%B %d, %Y")) 
        body = processReport()
        
        # Create pdf report using processed title and data
        reports.generate_report("/tmp/processed.pdf",title,body)

        # Collect information for report email
        sender="automation@example.com"
        recipient = "{}@example.com".format(os.environ.get('USER'))
        subject = "Upload Completed - Online Fruit Store"
        body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
        attachment_path = "/tmp/processed.pdf"

        # Generate and send email
        message = emails.generate_email(sender, recipient, subject, body, attachment_path)
        emails.send(message)