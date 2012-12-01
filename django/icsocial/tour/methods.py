# Create your views here.
from tour.models import *
from django.contrib.auth.models import User

def get_owner(name_of_tour):
	bs = Tour.objects.get(name=name_of_tour)
	owner_username = bs.owner_id.username
	return owner_username

def delete_tour(name_of_tour):
	bs = Tour.objects.filter(name=name_of_tour)
	bs.delete()

def get_subscribers(name_of_tour):
	bs = Tour.objects.get(name=name_of_tour)
	subscribers_list = bs.subscribers
	return subscribers_list

def get_date(name_of_tour):
	bs = Tour.objects.get(name=name_of_tour)
	date = bs.tour_date
	return date

def total_user_comments(id):
	return Comment.objects.filter(user=id).count()

def total_subs():
	return SubComment.objects.count()











