from django.db import models

# Create your models here.
class Users(models.Model):
    phone_number = models.CharField(max_length=11)
    user_password = models.CharField(max_length=6)
    address = models.CharField(max_length=100,default='buQYvwKqwE2m3Y8Vuoy79McXh68amDD7TaNS')
    public_key = models.CharField(max_length=200,default='privbxfPrswQWZ4YZQeFLrCviVvy8EkaBgPLNRR5EZzmVfUnhcSz2m3h')
    private_key = models.CharField(max_length=200,default='b001f9ab8f65ef228f1270a29e23de0920fbaf22403412ccd2ed7115ac68b5611de45aad0eb2')
    bool = models.NullBooleanField(default = False) #当前用户授权
    def __unicode__(self):
        return self.phone_number

class account(models.Model):
    ac_coins = models.DecimalField(default=50.00000000,max_digits =28,decimal_places =8)
    ac_users = models.ForeignKey(Users, on_delete=models.CASCADE)
    def _str_(self):
        return  self.ac_users