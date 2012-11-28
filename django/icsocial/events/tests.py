from django.test import TestCase
from django.utils import unittest
from events.models import *
from events.methods import *


class SimpleTest(unittest.TestCase):

    def test_is_added(self):
        Event.objects.create(title='koukou', nickname='kkokjfjfjfkos', location='huxley', date='2012-03-03', time='10:30', description='Work on our project.')
        self.assertEqual(get_event_count(), 2)


    def test_is_added_att(self):
        Attend.objects.create(attendee=2, event_id=15)
        self.assertEqual(get_allatt_count(), 12)


    def test_get_att_count(self):
        Attend.objects.create(attendee=2, event_id=2)
        self.assertEqual(get_att_count(2), 1)


    def test_get_user_events(self):
    	 Attend.objects.create(attendee=2, event_id=2)
    	 Attend.objects.create(attendee=2, event_id=3)
    	 self.assertTrue(2 in get_user_events(2))
    	 self.assertFalse(5 in get_user_events(2))


    def test_get_att_of_event(self):
    	 Attend.objects.create(attendee=2, event_id=2)
    	 Attend.objects.create(attendee=5, event_id=3)
    	 self.assertTrue(2 in get_att_of_event(2))
    	 self.assertTrue(5 in get_att_of_event(3))
    	 self.assertFalse(2 in get_att_of_event(3))

    def test_get_event_titles(self):
        Event.objects.create(title='koukou', nickname='kkokkos', location='huxley', date='2012-03-03', time='10:30', description='Work on our project.')
        Attend.objects.create(attendee=1, event_id=1)
        Attend.objects.create(attendee=1, event_id=2)
        Attend.objects.create(attendee=1, event_id=3)
        Attend.objects.create(attendee=1, event_id=4)
        Attend.objects.create(attendee=1, event_id=5)
        Attend.objects.create(attendee=1, event_id=6)
        self.assertFalse('koukou' in get_event_titles(1))
