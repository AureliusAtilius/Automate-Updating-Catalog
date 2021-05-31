#!/usr/bin/env python3
import requests
import os

def processDescription(file):

        # Split filename and file extension
        filename, fileExt = os.path.splitext(file)
        file=("/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))+file)
        jsonobj={}
        
        # Parse file information and convert to .json dictionary
        with open(file,"r") as file:
                lines = file.readlines()
                jsonobj["name"]=lines[0].rstrip("\n")
                jsonobj["weight"]= int((lines[1].rstrip("\n").replace(" lbs","")))
                jsonobj["description"]=lines[2].rstrip("\n")
                jsonobj["image_name"]=  filename+".jpeg"
        return jsonobj

def uploadDescription(jsonobj):

        # URL descriptions will be posted to.
        url="http://[linux-instance-IP-Address]/fruits/"   
        
        # Post
        response= requests.post(url, json=jsonobj)  
        print(response.status_code)

if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))):
                processed=processDescription(file)
                uploadDescription(processed)