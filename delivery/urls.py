from .views import (
                    addDeliveryModeView,
                    createDispatchView,
                    makeDeliveryView,
                    initiateDeliveryView,
                    deliveryPaymentView,
                    )
from django.urls import path


urlpatterns = [
    path ('addDeliveryMode/', addDeliveryModeView, name="addDeliveryMode_url"),
    path ('createDispatch/<id>',createDispatchView, name="createDispatch_url"),
    path ('makeDelivery/', makeDeliveryView, name="makeDelivery_url"),
    path ('initiateDelivery/<orderNumber>',initiateDeliveryView, name="initiateDelivery_url"),
    path ('deliveryPayment/<orderNumber>',deliveryPaymentView, name="deliveryPaymentView_url"),
] 