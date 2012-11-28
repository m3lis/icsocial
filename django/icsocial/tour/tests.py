"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.utils import unittest
from django.test import TestCase
from tour.models import Tour
from tour.methods import *
from django.contrib.auth.models import User


class SearchTestCase(unittest.TestCase):
	def test_get_owner(self):
		user1 = User.objects.create_user('John','j@j.com','j1')
		user2= User.objects.create_user('Mike','m@m.com','m1')
		user3= User.objects.create_user('kokoko','m@m.com','m1')
		user4= User.objects.create_user('lalal','m@m.com','m1')
		tour = Tour()
		tour.id = "1"
		tour.name = "hello"
		tour.owner_id = user1
		tour.save()
		self.assertEqual(get_owner("hello"),'John')

	def test_delete_tour(self):
		user1 = User.objects.create_user('kokokoko','j@j.com','j1')
		user2= User.objects.create_user('kk','m@m.com','m1')
		user3= User.objects.create_user('ff','m@m.com','m1')
		user4= User.objects.create_user('dd','m@m.com','m1')
		tour = Tour()
		tour.id = "1"
		n = tour.name = "hello"
		tour.owner_id = user1
		tour.save()
		delete_tour(n)
		tour1 = Tour()
		n1 = tour1.name = "hello"
		tour1.owner_id = user1
		tour1.save()
		self.assertEqual(get_owner("hello"), "kokokoko")

	def test_get_subsribers(self):
		user1= User.objects.create_user('Mar2','j@j.com','j1')
		user3= User.objects.create_user('koupepia','m@m.com','m1')
		user4= User.objects.create_user('Ginnis1','m@m.com','m1')
		tour = Tour()
		tour.owner_id = user1
		tour.save()
		tour.subscribers.add(user3, user4)
		tour.name = "Open Day"
		# tour.tour_date = "2010-12-12"
		tour.save()
		self.assertEqual(get_subscribers("Open Day").count(),2)
		# self.assertEqual(get_date("Open Day"), (2010,12,12))



