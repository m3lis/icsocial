"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.utils import unittest
from django.test import TestCase
from tour.models import *
from tour.methods import *
from django.contrib.auth.models import User


class SearchTestCase(unittest.TestCase):
	def test_get_owner(self):
		user1 = User.objects.create_user('John','j@j.com','j1')
		user2= User.objects.create_user('Mike','m@m.com','m1')
		user3= User.objects.create_user('Niki','m@m.com','m1')
		user4= User.objects.create_user('Nikolas','m@m.com','m1')
		tour = Tour()
		tour.id = "1"
		tour.name = "hello"
		tour.owner_id = user1
		tour.save()
		self.assertEqual(get_owner("hello"),'John')

	def test_delete_tour(self):
		user1 = User.objects.create_user('Kokos','j@j.com','j1')
		user2= User.objects.create_user('Michael','m@m.com','m1')
		user3= User.objects.create_user('Sakis','m@m.com','m1')
		user4= User.objects.create_user('Anna','m@m.com','m1')
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
		self.assertEqual(get_owner("hello"), "Kokos")

	def test_get_subsribers(self):
		user1= User.objects.create_user('Dan','j@j.com','j1')
		user3= User.objects.create_user('Giorgos','m@m.com','m1')
		user4= User.objects.create_user('Giannis','m@m.com','m1')
		tour = Tour()
		tour.owner_id = user1
		tour.save()
		tour.subscribers.add(user3, user4)
		tour.name = "Open Day"
		# tour.tour_date = "2010-12-12"
		tour.save()
		self.assertEqual(get_subscribers("Open Day").count(),2)
		# self.assertEqual(get_date("Open Day"), (2010,12,12))

	def test_total_user_comments(self):
		user_object = User.objects.create_user('Crestas','j@j.com','j1')
		subcomment = SubComment()
		comment = Comment()
		comment.user = user_object
		comment.save()
		comment2 = Comment()
		comment2.user = user_object
		comment2.save()
		subcomment.user = user_object
		subcomment.save()
		self.assertEqual(total_user_comments(user_object),3)

	def test_add_comment(self):
		user = User.objects.create_user('Melis','j@j.com','j1')
		add_comments(user)
		l = Location()
		l.name = 'Huxley'
		l.nickname = 'Hux'
		l.save()
		q = QuestionsNews()
		q.owner_id = user
		q.text = 'Why?'
		q.location = l
		q.category = 'Q'
		add_questions(q)
		self.assertEqual(calc_comments().count(),1)
		self.assertEqual(calc_questions().count(),1)



