from django.db import models
from login.models import Users
# Create your models here.
class Blacklist(models.Model):
    Bl_User = models.ForeignKey(Users, on_delete = models.CASCADE)

class Volunteer(models.Model):
    Vl_User = models.ForeignKey(Users, on_delete = models.CASCADE)
    Vl_Detail = models.CharField(max_length = 1000)