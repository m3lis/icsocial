"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from friendship.models import *
from friendship.methods import *
from django.test import TestCase
from django.contrib.auth.models import User


class FriendTestCase(unittest.TestCase):
	def test_is_friend(self):
		user1 = User.objects.create_user('John','j@j.com','j1')
		user2= User.objects.create_user('Mike','m@m.com','m1')
		friends = Friend();
		id_user1 = friends.id_user = user1
		id_user2 = friends.id_follower = user2
		friends.save()
		# first comes the follower id
		self.assertEqual(is_follower(id_user1,id_user2),False)
		self.assertEqual(is_follower(id_user2,id_user1),True)

	def test_get_followers(self):
		f = Friend();
		user = f.id_user = User.objects.create_user('Maria','j@j.com','j1')
		follower = f.id_follower = User.objects.create_user('Yiannis','m@m.com','m1')
		f.save()
		self.assertTrue(follower in get_followers(user))
		
