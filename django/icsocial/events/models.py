from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	title = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30, unique=True)
	location = models.CharField(max_length=20)
	date = models.DateField()
	time = models.TimeField()
	description = models.CharField(max_length=500)

class Attend(models.Model):
	attendee = models.IntegerField()
	event_id = models.IntegerField()


