from django.shortcuts import render
from urllib.request import urlopen
import json, urllib
from . import forms
import requests
import os

# Create your views here.

def home(request):
    f = forms.GrammerCheck()
    value = ""
    if request.method == "POST":
        data = forms.GrammerCheck(request.POST)
        if data.is_valid():
            value = data.cleaned_data["TextArea"]
        else:
            print("Error: data error")

    if value == "":
        return render(request, "home.html", {"value":value, "form":f, "wordcount":0,"charatercount": 0, "grammer":{'score':"100"}})
    else:
        return render(request, "home.html", {"value":value, "form":f, "wordcount":len(value.split()),"charatercount": len(value), "grammer":grammer(value)})

def grammer(value):
    value = value.encode('ascii', 'ignore').decode('utf-8')
    value = "+".join(value.split())
    API_key = os.environ.get("api")
    #url = "https://api.textgears.com/check.php?text=" + value + "&key=" + API_key

    try:
        url = "https://api.textgears.com/check.php"
        payload = "text={}&key={}".format(value, API_key)
        headers = {'content-type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
    except Exception as e:
        return {'score':"100", 'status':"Sorry! too large text. I'll fix this soon"}

    json_obj = response.json()
    json_obj["status"] = " "
    return json_obj
