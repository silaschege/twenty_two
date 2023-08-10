from django.contrib import admin
from .models import (ProductCategoryModel,
                     ProductModel,
                     ReceiveGoodsCategoryModel,
                     ReceiveGoodsCategoryModelHolder,
                     ReceiveGoodsDetailModel,
                     ReceiveGoodsDetailHolderModel
                     )

# Register your models here.
admin.site.register(ProductCategoryModel)
admin.site.register(ProductModel)
admin.site.register(ReceiveGoodsCategoryModel)
admin.site.register(ReceiveGoodsCategoryModelHolder)
admin.site.register(ReceiveGoodsDetailModel)
admin.site.register(ReceiveGoodsDetailHolderModel)
