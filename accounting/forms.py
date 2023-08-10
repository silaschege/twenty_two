from django import forms
from .models import SupplierBulkDebit,OrderDebit

class SupplierSearchForm(forms.Form):
    supplierSearchQuery = forms.CharField(
        label='Search Supplier',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class PartnerSearchForm(forms.Form):
    partnerSearchQuery = forms.CharField(
        label='Search partner',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class SupplierBulkDebitForm(forms.ModelForm):
    class Meta:
        model=SupplierBulkDebit
        fields=["supplier","bulkamount",]
        labels={
                "supplier":"Supplier",
                "bulkamount":"Amount",
        }
        widgets={
                "supplier":forms.Select(attrs={'class':'form-control'}),
                "bulkamount":forms.NumberInput(attrs={'class':'form-control'}),

        }

class OrderDebitForm(forms.ModelForm):
    class Meta:
        model=OrderDebit
        fields=['amount']
        label={
                'amount':"Amount Paid",
        }
        widgets={
                "amount":forms.NumberInput(attrs={'class':'form-control'}),
        }