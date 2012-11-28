from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse("home")

def login(request):

    return render_to_response('login.html', {})

def place(request,nick):
    return HttpResponse("location:" + nick)

def profile(request,nick):
 	return HttpResponse("profile:" + nick)