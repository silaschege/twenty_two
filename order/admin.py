from django.contrib import admin
from .models import OrderNumberPartner,OrderItemPartner,OrderNumberPartnerHolder,OrderItemPartnerHolder

# Register your models here.
admin.site.register(OrderNumberPartner)
admin.site.register(OrderItemPartner)
admin.site.register(OrderNumberPartnerHolder)
admin.site.register(OrderItemPartnerHolder)
