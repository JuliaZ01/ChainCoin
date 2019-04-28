from django.db import models
from login.models import Users
# Create your models here.
class Blacklist(models.Model):
    Bl_user = models.ForeignKey(Users, on_delete = models.CASCADE)
    def __str__(self):
        return self.Bl_user.phone_number

class Volunteer(models.Model):
    Vl_name = models.CharField(max_length = 500)
    Vl_user = models.ForeignKey(Users, on_delete = models.CASCADE)
    Vl_detail = models.CharField(max_length = 1000)
    def __str__(self):
        return self.Vl_name