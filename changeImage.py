#!/usr/bin/env python3
import os
from PIL import Image

def imageReformat(file):
        # Check if .TIFF file
        filename, fileExt = os.path.splitext("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
        if fileExt == ".tiff":
                im = Image.open("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
                resized_im = im.resize((600,400))
                #cannot convert from TIFF to JPEG, must convert to RGB first
                resized_im = resized_im.convert("RGB")

                resized_im.save(filename+'.jpeg', format= "JPEG")
                os.remove("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+filename+fileExt)

                
if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/images".format(os.environ.get('USER'))):
                imageReformat(file)