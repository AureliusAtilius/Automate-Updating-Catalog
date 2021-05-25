#!/usr/bin/env python3
import requests
import os
def imageUploader(image):
        url= "http://[linux-instance-IP-Address]/upload"
        with open(image,"rb") as image:
               r= requests.post(url, files={"file":image})

if __name__=="__main__":
        for file in os.listdir("~/supplier-data/images/"):
                filename, fileExt = os.path.splitext(file)
                if fileExt == ".jpg":
                        imageUploader(file)
