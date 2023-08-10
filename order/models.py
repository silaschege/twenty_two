from django.db import models
from django.conf import settings
from partner.models import PartnerBusiness
from product.models import ProductModel


# Create your models here.
class OrderNumberPartner(models.Model):
    partner = models.ForeignKey(PartnerBusiness,on_delete=models.SET_DEFAULT,default=1)
    orderBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=40)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return  self.order_number

class OrderItemPartner(models.Model):
    orderNumber = models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1)
    product = models.ForeignKey(ProductModel,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()


class OrderNumberPartnerHolder(models.Model):
    partner = models.ForeignKey(PartnerBusiness,on_delete=models.SET_DEFAULT,default=1)
    orderBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=40)

class OrderItemPartnerHolder(models.Model):
    orderNumber = models.ForeignKey(OrderNumberPartnerHolder,on_delete=models.SET_DEFAULT,default=1)
    product = models.ForeignKey(ProductModel,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()



    

