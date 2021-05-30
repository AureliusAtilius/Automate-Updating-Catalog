#!/usr/bin/env python3

from reportlab.platypus import paragraph
import os
import reports
import run


def  processReport():
        pdf_lines=[]
        for file in os.listdir("~/supplier-data/descriptions"):
                data=run.processDescription(file)
                name = "name: {}".format(data["name"])
                weight = "weight: {}".format(data["weight"])
                empty_line= "<br/>"
                pdf_lines.extend([name, weight,empty_line])
        pdf_data="<br/>".join(pdf_lines)        
        return pdf_data
if __name__=="__main__":
        title= "Uploaded Items"
        body = processReport()
        reports.generate_report("/tmp/processed.pdf",title,body)