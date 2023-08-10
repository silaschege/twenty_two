from django.db import models
from django.conf import settings
from delivery.models import Ontransit

class SaleNumberModel(models.Model):
    ontransitNumber= models.ForeignKey(Ontransit,on_delete=models.SET_DEFAULT,default=1)
    saleBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

   




