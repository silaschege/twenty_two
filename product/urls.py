from .views import (
                    addProductCategoryView,
                    addProductView,
                    allProductView,
                    receiveMerchandizeSupplierView,
                    receiveMerchandizeProductView,
                    finalizeReceiveProductsView,
                    productPricingView,

                    )
from django.urls import path


urlpatterns = [
        
    path ('addProductCategory/',addProductCategoryView, name="addProductCategory_url"),
    path ('addProduct/',addProductView, name="addProduct_url"),
    path ('allProduct/',allProductView, name="allProductView_url"),
    path ('receiveMerchandizeSupplier/',receiveMerchandizeSupplierView, name="receiveMerchandizeSupplier_url"),
    path ('receiveMerchandizeProduct/',receiveMerchandizeProductView, name="receiveMerchandizeProduct_url"),
    path ('finalizeReceiveProduct/',finalizeReceiveProductsView, name="finalizeReceiveProduct_url"),    
    path ('productPricing/',productPricingView, name="productPricing_url"),
] 