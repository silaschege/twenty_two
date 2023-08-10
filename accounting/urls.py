from .views import (
                    AllSupplierAccountsView,
                    supplierAcountDetailView,
                    supplierAccountDebitView,
                    allPartnerAccountsView,
                    partnerAccountStatementView,

                    )
from django.urls import path


urlpatterns = [
        
    path ('allsupplierAccount/',AllSupplierAccountsView, name="AllSupplierAccounts_url"),
    path ('supplierAccountDetail/<id>',supplierAcountDetailView, name="supplierAcountDetail_url"),
    path ('supplierAccountDebit/<id>', supplierAccountDebitView, name="supplierAccountDebit_url"),
    path ('allPartnerAccount/',allPartnerAccountsView, name="allPartnerAccount_url"),
    path ('partnerAccountStatement/<id>',partnerAccountStatementView, name="partnerAccountStatement_url"),
 
] 