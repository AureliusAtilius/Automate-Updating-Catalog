#!/usr/bin/env python3
import requests
import os

def processDescription(file):
        jsonobj={"name": "","weight":0,"description":"","image_name":""}
        with open(file,"r") as file:
                lines = file.readlines()
                jsonobj["name"]=lines[0].rstrip("\n")
                jsonobj["weight"]= int(lines[1].rstrip("\n"))
                jsonobj["description"]=lines[2].rstrip("\n")
                jsonobj["image_name"]=lines[3].rstrip("\n")