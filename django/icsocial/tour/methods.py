# Create your views here.
from tour.models import *
from django.contrib.auth.models import User


#Tour
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

#Comments
def total_user_comments(user1):
	return Comment.objects.filter(user=user1).count() + SubComment.objects.filter(user=user1).count()

def total_subs():
	return SubComment.objects.count()

def delete_comments(id):
	 c=Comment.objects.filter(user=id)
	 c.delete()

def calc_comments():
	return Comment.objects.all()

def add_comments(user1):
	 c = Comment()
	 c.user = user1
	 c.save()

#Locations
def get_names(na):
	b = Location.objects.filter(name__contains=na)
	return b

def get_address(ad):
   add = Location.objects.filter(address__contains=na)
   return add


# Questions
def calc_questions():
	return QuestionsNews.objects.filter(category='Q')

def add_questions(q):
	q.save()

def calc_news():
	return QuestionsNews.objects.filter(category='N')

def add_news(q):
	q.save()













