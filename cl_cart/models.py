from django.db import models

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey('cl_user.User',None)
    goods=models.ForeignKey('cl_goods.GoodInfo',None)
    count=models.IntegerField(default=0)