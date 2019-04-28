from django.contrib import admin
from .models import Blacklist
from .models import Volunteer

admin.site.register(Blacklist)
admin.site.register(Volunteer)
# Register your models here.
