from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from tour.methods import *



def nav(flag):
	#if flag == True then logged in else guest
	n = {'home':'home/','tour': {'buildings':'/places/','tours':'/tours/', 'mytours':'/mytours/'},\
	 	'about':{'social_ic':'/about/icsocial/','us':'/about/us/',\
	 	'tech':'/about/tech/'},'campus':'/campus/','logout':'/logout'}
	return n

def index(request):
	logged = request.user.is_authenticated()
	navi = nav(logged)
	c = {'nav': navi,'logged': logged}
	if logged:
		c['username'] = request.user.username
	c.update(csrf(request))
	return render_to_response("index.html",c)

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	if request.method != 'POST':
		return HttpResponse("login")
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			user_login(request, user)
			return HttpResponseRedirect("/")
		else:
			return HttpResponse("login: account disabled")
	else:
		return HttpResponse("wrong username/password")

def logout(request):
	if request.user.is_authenticated():
		HttpResponseRedirect("/")
	user_logout(request)
	return HttpResponseRedirect("/")

def place(request,nick):
    return HttpResponse("location:" + nick)

def profile(request,nick):
  return HttpResponse("profile:" + nick)

def tours(request):
	r= []
	tour = Tour.objects.all()

	for i in Tour.objects.all().values_list('id', flat=True):
		r.insert(len(r),i)

	for elem in r:
		name = get_name(elem)
		tour_date = get_date(elem)
		subscribers = get_subscribers(name)
		c = {'name':name, 'tour_date':tour_date, 'subscribers':subscribers, 'tour':tour}
		return render_to_response("tours.html",c)

def mytours(request):
	user = request.user
	if user.is_authenticated():
   	 user_id=user.pk
	r= []
	tour = Tour.objects.filter(owner_id= user_id)

	for i in Tour.objects.all().values_list('id', flat=True):
		r.insert(len(r),i)

	for elem in r:
		name = get_name(elem)
		tour_date = get_date(elem)
		subscribers = get_subscribers(name)
		c = {'name':name, 'tour_date':tour_date, 'subscribers':subscribers, 'tour':tour}
		return render_to_response("myTours.html",c)

def add_tour(request):
	tour = Tour();
	tour.name = request.POST['name']
	tour.tour_date = request.POST['tour_date']	
	tour.description = request.POST['description']
	tour.save()
	c = {'name':tour.name, 'tour_date':tour.tour_date, 'subscribers':tour.subscribers}
	return render_to_response("myTours.html",c)

def buildings(request):
	r= []
	building = Location.objects.all()
	for i in Location.objects.all().values_list('id', flat=True):
		r.insert(len(r),i)

	for elem in r:
		name = get_build_name(elem)
		description = get_build_desc(elem)
		c = {'name':name, 'description':description, 'building':building}
		return render_to_response("buildings.html",c)





