#!/usr/bin/env python3
import requests
import os
def imageUploader(image):
        url= "http://localhost/upload/"    
        with open(image,"rb") as image:
               r= requests.post(url, files={"file":image})

if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/images/".format(os.environ.get('USER'))):
                filename, fileExt = os.path.splitext("/home/{}/supplier-data/images/".format(os.environ.get('USER'))+file)
                if fileExt == ".jpeg":
                        imageUploader(filename+fileExt)
