from django.db import models

class StudentData(models.Model):
    name=models.CharField(max_length=100)
    marks=models.IntegerField()


