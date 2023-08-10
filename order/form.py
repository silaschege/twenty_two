from django import forms
from .models import OrderItemPartnerHolder
class SearchPartnerForm(forms.Form):
    query = forms.CharField(
        label='Search Partner',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class SearchProductForm(forms.Form):
    productSearch = forms.CharField(
        label='Search Product',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class OrderPartnerItemsHolderForm(forms.ModelForm):
    class Meta:
        model=OrderItemPartnerHolder
        fields = ["product","quantity"]
        labels={"product":"Product",
                "quantity":"Quantity ordered"
                }
        widgets={
                "product":forms.Select(attrs={'class': 'form-control'}),
                "quantity":forms.TextInput(attrs={'class': 'form-control'})
                }