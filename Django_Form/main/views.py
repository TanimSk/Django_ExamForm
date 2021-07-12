from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Question
from .delta_time import Delta_time
import requests
import json



def home(req):
    content = Question.objects.all()
    return render(req, "main/home/index.html", {'content': content})


def questions(req, ques_id):
    json_ques = Question.objects.get(pk=ques_id).json_ques
    content =  json.loads(json_ques)
    time_obj = Delta_time(content['starts'][0], content['starts'][1])

    if time_obj.h < 0 or (time_obj.h==0 and time_obj.m==0 and time_obj.s == 0):
        return render(req, "main/questions/question.html", {'json_ques': json_ques})
    else:
        return render(req, "main/questions/countdown.html", {'time_h': time_obj.h, 'time_m': time_obj.m, 'time_s': time_obj.s})


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

    return HttpResponse(json.dumps({'url': url}), content_type='application/json')


def write(req):
    if req.method == 'POST':
        json_ques = req.POST.get('json_ques')
        entry = Question(json_ques=json_ques, title=json.loads(json_ques)['title'])
        entry.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("ERROR!")
