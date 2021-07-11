from django.db import models


class Question(models.Model):
    json_ques = models.JSONField()
    title = models.CharField(max_length=120)
    # starts = models.CharField(max_length=10)
    # duration = models.IntegerField()

    # email = models.EmailField(max_length=200)
