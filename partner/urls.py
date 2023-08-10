from .views import (CreatePartnerView,
                    CreatePartnerAdminView,
                    CreateBusinessTypeView
                    )
from django.urls import path


urlpatterns = [
        
    path ('CreatePartner/',CreatePartnerView, name="CreatePartner_url"),
    path ('CreatePartnerAdmin/',CreatePartnerAdminView, name="CreatePartnerAdmin_url"),
    path ('CreateBusinessType/',CreateBusinessTypeView, name="CreateBusinessType_url"),
] 