from django.db import models
from login.models import Users
from projects.models import projects
# Create your models here.
class investbill(models.Model):
    iv_coins = models.IntegerField()
    iv_from = models.ForeignKey(Users, on_delete = models.CASCADE)
    iv_to = models.ForeignKey(projects, on_delete = models.CASCADE)
    iv_ps = models.CharField(max_length = 500)
    iv_time = models.DateTimeField(auto_now_add=True)