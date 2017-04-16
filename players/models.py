# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Players(models.Model):
    Name = models.CharField(max_length=128,primary_key=True)
    Nationality = models.CharField(max_length=128)

    class Meta:
        db_table = "footballers"

class Player(models.Model):
    Name = models.CharField(max_length=128, primary_key=True)
    Nationality = models.CharField(max_length=128)
    Club = models.CharField(max_length=128)
    National_Position = models.CharField(max_length=128)
    Rating = models.IntegerField()
    Age = models.IntegerField()
    Height = models.CharField(max_length=128)
    Weight = models.CharField(max_length=128)
    Preffered_Foot = models.CharField(max_length=128)
    Aggression = models.IntegerField()
    Freekick_Accuracy = models.IntegerField()
    Speed = models.IntegerField()
    Jumping = models.IntegerField()
    Shot_Power = models.IntegerField()
    Agility = models.IntegerField()

    class Meta:
        db_table = "footballers"
