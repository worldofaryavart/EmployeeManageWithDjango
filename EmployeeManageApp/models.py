from django.db import models


class Personal(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

class Office(models.Model):
    ecode = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    post = models.CharField(max_length=20)
    joining = models.CharField(max_length=10)
    basicpay = models.IntegerField()

class Salary(models.Model):
    ecode = models.CharField(max_length=10)
    months = models.IntegerField()
    overtime= models.IntegerField()
    finalpay = models.FloatField()

    def __str__(self):
        return f"{self.ecode} - {self.finalpay}"