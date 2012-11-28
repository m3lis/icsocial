from location.models import Location
from location.methods import get_names
from django.db import models
from django.contrib.auth.models import User

def search_loc(name):
	return get_names(name)

def search_usernames(na):
	names = User.objects.filter(username__startswith=na)
	return names

def search_firstnames(na):
	names = User.objects.filter(first_name__startswith=na)
	return names

def search_lastnames(na):
	names = User.objects.filter(last_name__startswith=na)
	return names

"""
def search_address(name):
	return get_address(name).count()
"""

