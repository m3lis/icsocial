from django.contrib import admin
from tour.models import *

admin.site.register(Location)
admin.site.register(Tour)
admin.site.register(Comment)
admin.site.register(SubComment)

