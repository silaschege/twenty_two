from django.db import models
from order.models import OrderNumberPartner
from django.conf import settings
from supplier.models import SupplierDetailModel
from product.models import ReceiveGoodsCategoryModel
from partner.models import PartnerBusiness
# Create your models here.
# making order
class OrderInvoice(models.Model):
    order =  models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1)
    amount = models.IntegerField()
  

# order captain
class InvoiceCaptain(models.Model):
    order =  models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1) 
    invoice = models.ForeignKey(OrderInvoice,on_delete=models.SET_DEFAULT,default=1)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



# orderpayment 
class OrderDebit(models.Model):
    order  =  models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1) 
    invoice =    models.ForeignKey(OrderInvoice,on_delete=models.SET_DEFAULT,default=1) 
    partner = models.ForeignKey(PartnerBusiness,on_delete=models.CASCADE)
    amount = models.IntegerField()

# order captain
class DebitCaptain(models.Model):
    order = models.ForeignKey(OrderNumberPartner,on_delete=models.SET_DEFAULT,default=1) 
    invoice =  models.ForeignKey(OrderInvoice,on_delete=models.SET_DEFAULT,default=1) 
    captain =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()

# supplier 
class SupplierInvoice(models.Model):
    supplier = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1) 
    receivedcategory = models.ForeignKey(ReceiveGoodsCategoryModel,on_delete=models.SET_DEFAULT,default=1) 
    receivedby =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()


# supplier bulk payment
class SupplierBulkDebit(models.Model):
    bulkamount = models.IntegerField()
    supplier = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1) 
    date = models.DateField(auto_now_add=True)
    paidby =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class SupplierPaymentBalance(models.Model):
    supplier  = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1) 
    receivedcategory = models.ForeignKey(ReceiveGoodsCategoryModel,on_delete=models.SET_DEFAULT,default=1) 
    paidby =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bulkpayment = models.ForeignKey(SupplierBulkDebit,on_delete=models.SET_DEFAULT,default=1)
    paid_amount = models.IntegerField()

# supplier single order debit
class SupplierDebit(models.Model):
    supplier  = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1) 
    receivedcategory = models.ForeignKey(ReceiveGoodsCategoryModel,on_delete=models.SET_DEFAULT,default=1) 
    paidby =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bulkpayment = models.ForeignKey(SupplierBulkDebit,on_delete=models.SET_DEFAULT,default=1)
    amount = models.IntegerField()
