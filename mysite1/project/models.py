# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Facilities(models.Model):
    Name = models.CharField(max_length=30)
	Location = models.CharField(max_length=100)
	Type = models.CharField(max_length=20)

	
class Neighbor(models.Model):
	Name = models.CharField(max_length=30)

class Reservations(models.Model):
    FacilityName = models.ForeignKey(Facilities, on_delete=models.CASCADE)
	NationalID = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
	Date = models.CharField(max_length=20)
	Time = models.CharField(max_length=20)
    Duration = models.IntegerField(default=0)
	
# Create your models here.
