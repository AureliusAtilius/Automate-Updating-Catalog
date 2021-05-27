#!/usr/bin/env python3
import run
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def reportgenerator():
        styles = getSampleStyleSheet()
        report = SimpleDocTemplate("processed.pdf")     #TODO: Add full file path to saved file
        empty_line = Spacer(1,20)
        pdf_file=[]
        for file in os.listdir("~/supplier-data/descriptions"):
                data=run.processDescription(file)
                name = Paragraph(data["name"], styles["BodyText"])
                weight = Paragraph(data["weight"], styles["BodyText"])
                pdf_file.extend([name, weight,empty_line])
        report.build(pdf_file)
                
