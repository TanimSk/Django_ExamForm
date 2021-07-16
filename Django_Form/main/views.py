from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Question, Student
from .delta_time import Delta_time
from . import Cdate
import requests
import json


def home(req):
    content = Question.objects.all()
    return render(req, "main/home/index.html", {'content': content})


def questions(req, ques_id):
    content = Question.objects.get(pk=ques_id).json_ques
    time_obj = Delta_time(content['starts'])

    if content['duration'] + time_obj.passed_s < 0 or content['date'] != Cdate.this_date():
        return redirect('/')

    elif time_obj.passed_s <= 0:
        if req.method == 'POST':
            name = req.POST.get('name')
            email = req.POST.get('email')
            number = req.POST.get('number')
            response_ans = req.POST.get('response_ans')
            print(response_ans, json.dumps(content))
            entry = Student(name=name, phone_number=number, email=email, ques_id=ques_id)
            entry.save()
            requests.post('http://127.0.0.1:5000/csv_manager', data={'mode': 'w', 'filename': f"chondro_bindu/{ques_id}.csv", 'key': 'KEY', 'ques_json': json.dumps(content), 'ans_json': response_ans})

            return HttpResponse(json.dumps({'done': True}), content_type='application/json')

        return render(req, "main/questions/question.html", {'title': content['title'], 'ques_qa': content['ques_qa'],
                                                            'ques_mcq': content['ques_mcq'], 'mcq': content['mcq'],
                                                            'images': content['images'],
                                                            'remaining_time': content['duration'] + time_obj.passed_s})
    else:
        return render(req, "main/questions/countdown.html", {'time_h': time_obj.h, 'time_m': time_obj.m,
                                                             'time_s': time_obj.s})


@login_required(login_url='login')
def admin_dashboard(req, redirect_url):
    if req.method == 'POST':
        json_ques = json.loads(req.POST.get('json_ques'))
        json_ques['date'] = Cdate.this_date()
        csv_field = req.POST.get('csv_field')
        print(csv_field)
        entry = Question(json_ques=json_ques, title=json_ques['title'])
        entry.save()
        requests.post('http://127.0.0.1:5000/csv_manager', data={'mode': 'wh', 'filename': f"chondro_bindu/{entry.id}.csv", 'row': csv_field, 'key': 'KEY'})
        return HttpResponse(json.dumps({'done': True}), content_type='application/json')

    if redirect_url == 'create':
        return render(req, "main/AdminPage/create_question.html")

    elif redirect_url == 'result':
        return HttpResponse("hello")

    elif redirect_url == 'main':
        return render(req, "main/AdminPage/dashboard.html")

    else:
        return HttpResponse("<h1>ERROR!</h1>")


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
