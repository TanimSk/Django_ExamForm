from django.db import models


class Question(models.Model):
    json_ques = models.JSONField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title       # its a tag, it represents Question type || Object Ques ->title


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    response_ans = models.JSONField()
    ques_id = models.IntegerField()
    def __str__(self):
        return self.name
