#!/usr/bin/env python3
import os
from PIL import Image
from pathlib import Path

def imageReformat(file):
        # Check if .TIFF file
        filename, fileExt = os.path.splitext(file)
        if fileExt == ".TIFF":
                im = Image.open(file)
                resized_im = im.resize((600,400))
                #cannot convert from TIFF to JPEG, must convert to RGB first
                resized_im = resized_im.convert("RGB")
        
                resized_im.save("<filepath>"+filename, format= "JPEG")

                #TODO: Upload to web service
