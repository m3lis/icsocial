from location.models import Location

def get_names(na):
	b = Location.objects.filter(name__contains=na)
	return b

def get_address(ad):
   add = Location.objects.filter(address__contains=na)
   return add
	

