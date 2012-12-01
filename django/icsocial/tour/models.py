from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
	name = models.CharField(max_length=30)
	#type = models.CharField(max_length=20) drop down list
	nickname = models.CharField(max_length=20, unique=True)
	parent = models.ForeignKey('self', null=True, blank=True)
	coordX = models.CharField(max_length=15)
	coordY = models.CharField(max_length=15)
	address = models.CharField(max_length=80)

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

class SubComment(models.Model):
	user = models.ForeignKey(User)
	text = models.CharField(max_length=200)
	date = models.DateField(null=True)
	time = models.TimeField(null=True)

class Comment(models.Model):
	user = models.ForeignKey(User)
	text = models.CharField(max_length=200)
	date = models.DateField(null=True)
	time = models.TimeField(null=True)
	subcom = models.ForeignKey(SubComment, related_name="com2", null=True)

POST_CHOICES = (
    ('N', 'News'),
    ('Q', 'Questions'),
)

class QuestionsNews(models.Model):
	owner_id =  models.ForeignKey(User)
	text = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	category = models.CharField(max_length=1, choices=POST_CHOICES)
	users = models.ForeignKey(Comment, related_name="com", null=True)






    

