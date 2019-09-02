from django.db import models


class APPoliceInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    location=models.CharField(max_length=100)



class TSpoliceInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    location = models.CharField(max_length=100)



