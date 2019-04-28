from django.db import models
from login.models import Users
# Create your models here.

class projects(models.Model):
    pjts_name = models.CharField(max_length=200)
    pjts_detail = models.CharField(max_length=400)
    pjts_users = models.ForeignKey(Users,on_delete=models.CASCADE)
    pjts_coins = models.DecimalField(max_digits =28,decimal_places =8)
    pjts_time = models.DateTimeField(auto_now_add=True,editable=True)
    pjts_nowcoins = models.DecimalField(max_digits =28,decimal_places =8,default=0) #现在已经有的币数
    pjts_now = models.NullBooleanField(default= True) #当前项目的状态
    pjts_address = models.CharField(max_length=400)
    pjts_hash = models.CharField(max_length = 400,default='false')
    pjts_bool = models.NullBooleanField(default = False)#当前项目上链与否
    def __str__(self):
        return self.pjts_name
