from django.db import models
from events.models import *

def get_event_count():
	return Event.objects.count()

def get_allatt_count():
	return Attend.objects.count()

def get_att_count(eve):
	return Attend.objects.filter(event_id=eve).count()

def get_user_events(atte):
	r = []
	bs = Attend.objects.filter(attendee=atte)
	for b in bs:
		r.insert(len(r),b.event_id)
	return r


def get_att_of_event(eve):
	r = []
	bs = Attend.objects.filter(event_id=eve)
	for b in bs:
		r.insert(len(r),b.attendee)
	return r

def get_event_titles(atte):
   r = []
   titles = []
   bs = Attend.objects.filter(attendee=atte)
   for b in bs:
		r.insert(len(r),b.event_id)
   for a in r:
		obj_eve = Event.objects.filter(id=a)
   for c in obj_eve:
		titles.insert(len(titles),c.title)
   return titles


	