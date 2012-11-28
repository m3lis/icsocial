from django.db import models

class Friend(models.Model):
   id_user = models.IntegerField()
   id_follower = models.IntegerField()

   def __unicode__(self):
      return self.id_user

   def get_friends(self):
      return self.id_follower

  

