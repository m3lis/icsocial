from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

def nav(flag):
	#if flag == True then logged in else guest
	n = {'home':'home/','tour': {'buildings':'/places/','tours':'/tours/'},\
	 	'about':{'social_ic':'/about/icsocial/','us':'/about/us/',\
	 	'tech':'/about/tech/'},'campus':'/campus/','logout':'/logout'}
	return n

def tour(request):
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