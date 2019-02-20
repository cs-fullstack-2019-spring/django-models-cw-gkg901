from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)


class Account(models.Model):
    username = models.CharField(max_length=30)
    realName = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(max_digits=99999999999,decimal_places=2)
