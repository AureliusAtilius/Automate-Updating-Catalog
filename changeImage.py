#!/usr/bin/env python3
import os
from PIL import Image

def imageReformat(file):
        # Split filename and extension
        filename, fileExt = os.path.splitext("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
       
        # Check if .tiff file
        if fileExt == ".tiff":
                im = Image.open("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
                
                # Resize image
                resized_im = im.resize((600,400))
                
                #cannot convert from TIFF to JPEG, must convert to RGB first
                resized_im = resized_im.convert("RGB")

                # Save image as jpeg
                resized_im.save(filename+'.jpeg', format= "JPEG")
                
                # Remove previous .tiff version of image
                os.remove(filename+fileExt)

                
if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/images".format(os.environ.get('USER'))):
                imageReformat(file)