from django.db import models
from django.contrib.auth.models import User
from location.models import Location

class Tour(models.Model):
	""" This is not the id is a User object
	"""
	owner_id = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	location = models.ManyToManyField(Location)
	subscribers = models.ManyToManyField(User, related_name="sub")
	tour_date = models.DateField(null=True)

	def get_owner_id(self):
		return self.owner_id

class Comment(models.Model):
	user = models.IntegerField()
	text = models.CharField(max_length=200)
	date = models.DateField()
	time = models.TimeField()
	
class SubComment(models.Model):
	user = models.IntegerField()
	parent = models.IntegerField()
	text = models.CharField(max_length=200)
	date = models.DateField()
	time = models.TimeField()








    

