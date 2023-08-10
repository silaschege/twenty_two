from .views import (createPartnerOrderView,
                    createPartner,
                    createPartnerOrderItemView,
                    createOrderItemInstanceView,
                    orderListView,
                    )
from django.urls import path


urlpatterns = [
        
    path ('CreatePartnerOrder/',createPartnerOrderView, name="createPartnerOrder_url"),
    path ('CreatePartner/<id>',createPartner, name="createPartner_url"),
    path ('createPartnerOrderItem/',createPartnerOrderItemView, name="createPartnerOrderItem_url"),
    path ('createOrderItemInstance/',createOrderItemInstanceView, name="createOrderItemInstance_url"),
    path ('orderList/',orderListView, name="orderList_url"),

 
] 