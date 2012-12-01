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
	b = Location.objects.filter(name=na)
	return b

def get_address(ad):
   add = Location.objects.filter(address=na)
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

def add_vote(vote):
	vote.save()

def calc_votes_agree():
	return Vote.objects.filter(category='A')

def calc_votes_user_agree(user):
	return Vote.objects.filter(category='A',user_voted=user)

def calc_votes_disagree():
	return Vote.objects.filter(category='D')

def calc_votes_user_disagree(user):
	return Vote.objects.filter(category='D',user_voted=user)

def calc_votes_obsolete():
	return Vote.objects.filter(category='O')

def calc_votes_user_obsolete(user):
	return Vote.objects.filter(category='O',user_voted=user)

def delete_vote(u1, c1):
	c=Vote.objects.filter(user_voted = u1,comment_voted = c1)
	c.delete()







