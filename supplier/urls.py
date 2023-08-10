from .views import (createSupplierView

                    )
from django.urls import path


urlpatterns = [
        
    path ('createSupplier/',createSupplierView, name="createSupplier_url"),
] 