"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.utils import unittest
from django.test import TestCase
from location.methods import get_names
from location.models import *
from search.methods import *

class SearchTestCase(unittest.TestCase):
	def test_search_loc(self):
	 f = Location.objects.create(name='Huxley')
	 self.assertEqual(search_loc('H').count(),1)

	def test_search_usernames(self):
	 n1 = User.objects.create_user('Yiannis','j@com','j1')
	 n2 = User.objects.create_user('Yiorkos','j@j.com','j2')
	 n3 = User.objects.create_user('MYiorkos','j@j.com','j2')
	 self.assertEqual(search_usernames('Yi').count(),2)
	 self.assertEqual(search_usernames('Y').count(),2)
	 self.assertEqual(search_usernames('Yio').count(),1)


	def test_search_firstnames(self):
	 f = User.objects.create_user('kokos', 'j@com','j1')
	 g = User.objects.create_user('kotsios','j@j.com','j2')
	 h = User.objects.create_user('koukou','j@j.com','j2')
	 f.first_name = 'Youa'
	 f.save()
	 g.first_name = 'Yiouia'
	 g.save()
	 h.first_name = 'Ioua'
	 h.save()
	 self.assertEqual(search_firstnames('Y').count(),2)
	 self.assertEqual(search_firstnames('Yio').count(),1)


	def test_search_lastnames(self):
	 f = User.objects.create_user('kokjhjhos', 'j@com','j1')
	 g = User.objects.create_user('kobfhftsios','j@j.com','j2')
	 h = User.objects.create_user('koukhhhou','j@j.com','j2')
	 f.last_name = 'Yiyis'
	 g.last_name = 'Yioyihusdis'
	 h.last_name = 'KYioua'
	 h.save()
	 g.save()
	 f.save()
	 self.assertEqual(search_lastnames('Y').count(),2)
	 self.assertEqual(search_lastnames('Yio').count(),1)

"""
	def test_search_ad(self):
	 dd = Location.objects.create(address='Queens')
	 ff = Location.objects.create(address='Queens1')
	 self.assertEqual(search_loc('Q'),1)
"""		
