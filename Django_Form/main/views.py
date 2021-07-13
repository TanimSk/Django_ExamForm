from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Question, Student
from .delta_time import Delta_time
import requests
import json


def home(req):
    content = Question.objects.all()
    return render(req, "main/home/index.html", {'content': content})


def questions(req, ques_id):
    content = json.loads(Question.objects.get(pk=ques_id).json_ques)
    time_obj = Delta_time(content['starts'])

    # if req.method == 'POST':
    #
    #     entry = Student(name=, phone_number=, email=, response_ans=,)
    #     entry.save()

    if time_obj.passed_s <= 0:
        return render(req, "main/questions/question.html", {'title': content['title'], 'ques_qa': content['ques_qa'], 'ques_mcq': content['ques_mcq'], 'mcq': content['mcq'], 'images': content['images'] ,'remaining_time': content['duration'] + time_obj.passed_s})
    else:
        return render(req, "main/questions/countdown.html", {'time_h': time_obj.h, 'time_m': time_obj.m, 'time_s': time_obj.s})



@login_required(login_url='login')
def page_admin(req):
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


def auth_login(req):
    if req.method == 'POST':
        handle = req.POST['handle']
        password = req.POST['password']
        user = authenticate(req, username=handle, password=password)
        if user is not None:
            login(req, user)
            return HttpResponse(json.dumps({'is_user': True}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'is_user': False}), content_type='application/json')
    else:
        return render(req, "main/login/index.html")
