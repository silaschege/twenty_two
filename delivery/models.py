from django.db import models
from order.models import OrderNumberPartner
from django.conf import settings

# Create your models here.
class DeliveryMode(models.Model):
    number_plate= models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    carrying_weight = models.IntegerField()
    carrying_weight_metric = models.CharField(max_length=25)
    carrying_size = models.IntegerField()

    def __str__(self):
        return  self.number_plate

class Ontransit(models.Model):
    orderNumber = models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1)
    deliveryMode = models.ForeignKey(DeliveryMode,on_delete=models.SET_DEFAULT,default=1)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class DeliveredOrder(models.Model):
    orderNumber = models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1)
    deliveryMode = models.ForeignKey(DeliveryMode,on_delete=models.SET_DEFAULT,default=1)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
