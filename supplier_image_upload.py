#!/usr/bin/env python3
import requests
import os

def imageUploader(image):
        
        # URL images will be posted to
        url= "http://localhost/upload/"    
        
        # Open file as binary
        with open(image,"rb") as image:
               
               # Post image
               r= requests.post(url, files={"file":image})

if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/images/".format(os.environ.get('USER'))):
                
                # Split filenam and extension
                filename, fileExt = os.path.splitext("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
                
                # Check if file is jpeg and upload it
                if fileExt == ".jpeg":
                        imageUploader(filename+fileExt)
