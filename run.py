#!/usr/bin/env python3
import requests
import os

def processDescription(file):
        filename, fileExt = os.path.splitext(file)
        file=("/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))+file)
        jsonobj={}
        with open(file,"r") as file:
                lines = file.readlines()
                jsonobj["name"]=lines[0].rstrip("\n")
                jsonobj["weight"]= int((lines[1].rstrip("\n").replace(" lbs","")))
                jsonobj["description"]=lines[2].rstrip("\n")
                jsonobj["image_name"]=  filename+".jpeg"
        return jsonobj

def uploadDescription(jsonobj):
        url="http://[linux-instance-IP-Address]/fruits/"   #TODO: Add IP
        response= requests.post(url, json=jsonobj)  
        print(response.status_code)
if __name__=="__main__":
        for file in os.listdir("/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))):
                processed=processDescription(file)
                uploadDescription(processed)