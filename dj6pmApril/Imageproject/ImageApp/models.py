from django.db import models


class Iamge(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    age=models.IntegerField()
    photo=models.ImageField(upload_to='images/')
