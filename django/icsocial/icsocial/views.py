from django.http import HttpResponse
from django.shortcuts import render_to_response

def nav(flag):
	#if flag == True then logged in else guest
	n = {'home': "/" ,'tour': {'buildings':'/places/','tours':'/tours/'},\
			'about':{'social_ic':'/about/icsocial/','us':'/about/us/',\
			'tech':'/about/tech/'},'campus':'/campus/'}

	n['tour']['my'] = '/my/tours/' 
	return n

def index(request):
	navi = nav(False)
	c = {'nav': nav}
	return render_to_response("index.html",c)

def login(request):
	return HttpResponse("login")

def place(request,nick):
    return HttpResponse("location:" + nick)

def profile(request,nick):
  return HttpResponse("profile:" + nick)

def dummy(request,title):
  return HttpResponse("title:" + title)