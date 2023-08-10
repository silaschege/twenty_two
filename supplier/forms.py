from django import forms
from .models import SupplierDetailModel

class createSupplierForm(forms.ModelForm):
    class Meta:
        model = SupplierDetailModel
        fields =[
                "supplier_name",
                "supplier_email_address",
                "supplier_phone_number",
                "supplier_kra_pin",
                "supplier_bank_1",
                "supplier_bank_1_number",
                "supplier_bank_2",
                "supplier_bank_2_number",

        ]
        labels={
               "supplier_name":"Name",
                "supplier_email_address":"Email",
                "supplier_phone_number":"Phone Number",
                "supplier_kra_pin":"KRA PIN",
                "supplier_bank_1":"Option Bank 1 Name",
                "supplier_bank_1_number":"Option Bank 1 Number",
                "supplier_bank_2":"Option Bank 2 Name",
                "supplier_bank_2_number":"Option Bank 2 Number",

        }
        widgets={
                "supplier_name":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_email_address":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_phone_number":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_kra_pin":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_bank_1":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_bank_1_number":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_bank_2":forms.TextInput(attrs={'class':'form-control'}),
                "supplier_bank_2_number":forms.TextInput(attrs={'class':'form-control'}),

        }