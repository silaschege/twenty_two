from django.db import models
from django.conf import settings

# Create your models here.
class businessType(models.Model):
    typeOfBusiness = models.CharField(max_length=255)
    def __str__(self):
        return  self.typeOfBusiness
    

class PartnerBusiness(models.Model):
    businessName = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street= models.CharField(max_length=255)
    businessLocation= models.CharField(max_length=255)
    businessType = models.ForeignKey(businessType, on_delete=models.CASCADE)
    registerBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    

class PartnerAdmin(models.Model):
    business = models.ForeignKey(PartnerBusiness, on_delete=models.CASCADE)
    firstName= models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    otherName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    adminId = models.CharField(max_length=255) 

