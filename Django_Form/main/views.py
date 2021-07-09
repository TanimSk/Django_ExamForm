from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login
from . import models
import json


def home(req):
    content = requests.get('http://127.0.0.1:5000/get_title')
    return render(req, "main/home/index.html", {'content': (content.text)})


def page_admin(req):
    # if req.method == 'POST':
    #     handle = req.POST['handle']
    #     password = req.POST['password']
    #     user = authenticate(req, username=handle, password=password)
    #     if user is not None:
    #         login(req, user)
    #         return render(req, "main/pageAdmin/index.html")
    #     else:
    #         return HttpResponse("wrong")
    # else:
    #     return render(req, "main/login/index.html")
    return render(req, "main/pageAdmin/index.html")


def upload_img(req):
    img64 = req.POST.get('base64_data')

    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": "bbbcf324565e027777302dbe3303c622",
        "image": img64,
        "expiration": '172800',
    }
    url = requests.post(url, payload).json()['data']['url']
    print(url)

    return HttpResponse(json.dumps({'url': url}), content_type='application/json')


def write(req):
    if req.method == 'POST':
        json_ques = req.POST.get('json_ques')
        entry = models.Questions(json_ques=json_ques)
        entry.save()
