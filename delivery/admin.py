from django.contrib import admin
from .models import DeliveryMode,Ontransit,DeliveredOrder

# Register your models here.
admin.site.register(DeliveryMode)
admin.site.register(Ontransit)
admin.site.register(DeliveredOrder)

