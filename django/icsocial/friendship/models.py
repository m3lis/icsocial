from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
	id_user = models.ForeignKey(User,related_name="id1")
	id_follower = models.ForeignKey(User)

	def __unicode__(self):
		return self.id_user

	def get_friends(self):
		return self.id_follower

  

