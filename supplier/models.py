from django.db import models

# Create your models here.
class SupplierDetailModel(models.Model):
    supplier_name = models.CharField(max_length=255)
    supplier_email_address = models.CharField(max_length=255)
    supplier_phone_number = models.CharField(max_length=255)
    supplier_kra_pin = models.CharField(max_length=255)
    supplier_bank_1 = models.CharField(max_length=255)
    supplier_bank_1_number = models.CharField(max_length=255)
    supplier_bank_2 = models.CharField(max_length=255)
    supplier_bank_2_number = models.CharField(max_length=255)
    

    def __str__(self):
        return  self.supplier_name