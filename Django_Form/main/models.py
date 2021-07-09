from django.db import models


class Questions(models.Model):
    ques_json = models.JSONField()
    # starts = models.CharField(max_length=10)
    # duration = models.IntegerField()
    # title = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200)

