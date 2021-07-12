from django.db import models


class Question(models.Model):
    json_ques = models.JSONField()
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title       #its a tag, it represents Question type || Object Ques ->title
