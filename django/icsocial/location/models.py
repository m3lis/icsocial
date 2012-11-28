from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=30)
	#type = models.CharField(max_length=20) drop down list
	nickname = models.CharField(max_length=20, unique=True)
	parent = models.ForeignKey('self', null=True, blank=True)
	coordX = models.CharField(max_length=15)
	coordY = models.CharField(max_length=15)
	address = models.CharField(max_length=80)



