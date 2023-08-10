from django.db import models
from supplier.models import SupplierDetailModel
from django.conf import settings

# Create your models here.
class ProductCategoryModel(models.Model):
    product_category_name = models.CharField(max_length=255)

    def __str__(self):
        return  self.product_category_name

class ProductModel(models.Model):
    product_category =  models.ForeignKey(ProductCategoryModel,on_delete=models.SET_DEFAULT,default=1)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_price = models.IntegerField()
    packaging_quantity = models.IntegerField()
    product_quantity = models.IntegerField() 
    product_image = models.ImageField(upload_to='product_images/',default='media/')

    def __str__(self):
        return  self.product_name
    
class ReceiveGoodsCategoryModel(models.Model):
    supplier = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1)
    receivedBY = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.IntegerField()

class ReceiveGoodsDetailModel(models.Model):
    receive_goods_category  =  models.ForeignKey(ReceiveGoodsCategoryModel,on_delete=models.SET_DEFAULT,default=1)
    product =  models.ForeignKey(ProductModel,on_delete=models.SET_DEFAULT,default=1)
    buying_price = models.IntegerField()
    quantity = models.IntegerField()
    selling_price =  models.IntegerField()

class ReceiveGoodsCategoryModelHolder(models.Model):
    supplier = models.ForeignKey(SupplierDetailModel,on_delete=models.SET_DEFAULT,default=1)
    receivedBY = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   


class ReceiveGoodsDetailHolderModel(models.Model):
    receive_goods_category  =  models.ForeignKey(ReceiveGoodsCategoryModelHolder,on_delete=models.SET_DEFAULT,default=1)
    product =  models.ForeignKey(ProductModel,on_delete=models.SET_DEFAULT,default=1)
    buying_price = models.IntegerField()
    quantity = models.IntegerField()
