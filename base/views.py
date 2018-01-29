from django.shortcuts import render
from urllib.request import urlopen
import json
from . import forms

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
        return render(request, "home.html", {"value":value, "form":f,"wordcount":0,"charatercount": 0, "grammer":{'score':"100"}})
    else:
        return render(request, "home.html", {"value":value, "form":f,"wordcount":len(value.split()),"charatercount": len(value), "grammer":grammer(value)})

def grammer(value):
    demo_key = "gg45GBEz4h7h8T73"
    value = "+".join(value.split())

    url = "https://api.textgears.com/check.php?text=" + value + "&key=" + demo_key
    response = urlopen(url)
    s = response.read().decode('utf-8')
    json_obj = json.loads(s)
    return json_obj
