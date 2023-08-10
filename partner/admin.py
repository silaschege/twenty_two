from django.contrib import admin
from .models import PartnerBusiness,PartnerAdmin,businessType

# Register your models here.
admin.site.register(PartnerBusiness)
admin.site.register(PartnerAdmin)
admin.site.register(businessType)