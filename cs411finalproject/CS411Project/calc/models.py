from django.db import models
from djongo import models as mo

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    height = models.IntegerField()
    race = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)
    companyname = models.CharField(max_length=30)
    age = models.IntegerField()

class School(models.Model):
    schoolname = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=25)
    conference = models.CharField(max_length=25)
    rank = models.IntegerField()

class Company(models.Model):
    companyname = models.CharField(max_length=50, primary_key=True)
    industry = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Perference(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    gender = models.CharField(max_length=20)
    heightlowbound = models.IntegerField()
    heighthighbound = models.IntegerField()
    agelowbound = models.IntegerField()
    agehighbound = models.IntegerField()
    race = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)
    companyname = models.CharField(max_length=30)

class Suggestions(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    suggested = models.CharField(max_length=10)

class Users(mo.Model):
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    class Meta:
        app_label = 'user_data'


