#!/usr/bin/env python3
import run
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title,body):
        styles = getSampleStyleSheet()
        report = SimpleDocTemplate(attachment)     
        report_title = Paragraph(title, styles["h1"])
        report_info = Paragraph(body, styles["BodyText"])
        empty_line = Spacer(1,20)
        pdf_file=[report_title,empty_line, report_info]
        
        report.build(pdf_file)
                
