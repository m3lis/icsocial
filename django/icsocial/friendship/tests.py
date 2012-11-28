"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from friendship.models import *
from friendship.views import *
from friendship.methods import *
from django.test import TestCase
from django.contrib.auth.models import User


class FriendTestCase(unittest.TestCase):
	def test_is_friend(self):
		user1 = User.objects.create_user('John','j@j.com','j1')
		user2= User.objects.create_user('Mike','m@m.com','m1')
		id_user1 = User.objects.get(username='John').id
		id_user2 = User.objects.get(username='Mike').id
		self.assertEqual(is_follower(id_user1,id_user2),False)
		self.assertEqual(is_follower(id_user2,id_user1),False)
		f = Friend.objects.create(id_user=id_user1,id_follower=id_user2)
		self.assertEqual(is_follower(id_user1,id_user2),False)
		self.assertEqual(is_follower(id_user2,id_user1),True)

	def test_get_followers(self):
		Friend.objects.create(id_user=6,id_follower=5)
		self.assertTrue(5 in get_followers(6))
		
