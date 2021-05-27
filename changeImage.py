#!/usr/bin/env python3
import os
import requests
from PIL import Image

def imageReformat(file):
        # Check if .TIFF file
        filename, fileExt = os.path.splitext(file)
        if fileExt == ".TIFF":
                im = Image.open(file)
                resized_im = im.resize((600,400))
                #cannot convert from TIFF to JPEG, must convert to RGB first
                resized_im = resized_im.convert("RGB")
        
                resized_im.save("~/supplier-data/images/"+filename, format= "JPEG")
        

                
if __name__=="__main__":
        for file in os.listdir("~/supplier-data/images"):
                imageReformat(file)