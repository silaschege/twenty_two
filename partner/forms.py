from django import forms
from .models import PartnerBusiness,PartnerAdmin,businessType

class CreateBusinessTypeForm(forms.ModelForm):
    class Meta:
        model = businessType
        fields = ['typeOfBusiness']
        labels={
            "typeOfBusiness":"Type Of Business"
        }
        widgets={
            "typeOfBusiness":forms.TextInput(attrs={"class": "form-control"}),
        }

class CreatePartnerBusinessForm(forms.ModelForm):
    class Meta:
        model = PartnerBusiness
        fields=["businessName","county","town","street","businessLocation","businessType",]
        labels={ "businessName":"Business Name",
                "county":"County",
                "town":"Town",
                "street":"Street",
                "businessLocation":"Business Location",
                "businessType":"Business Type",
                }
        widgets={
            "businessName":forms.TextInput(attrs={"class": "form-control"}),
            "county":forms.TextInput(attrs={"class": "form-control"}),
            "town":forms.TextInput(attrs={"class": "form-control"}),
            "street":forms.TextInput(attrs={"class": "form-control"}),
            "businessLocation": forms.TextInput(attrs={"class": "form-control"}),
            "businessType":forms.Select(attrs={'class':'form-control'}),
        }

class CreatePartnerAdminForm(forms.ModelForm):
    class Meta:
        model = PartnerAdmin
        fields=[ "firstName","lastName","otherName","phoneNumber","adminId", ]
        labels={
        "firstName":"First Name",
        "lastName":"Last Name",
        "otherName":"Other Name",
        "phoneNumber":"Phone Number",
        "adminId":"ID",
        }
        widgets={
        "firstName":forms.TextInput(attrs={"class": "form-control"}),
        "lastName":forms.TextInput(attrs={"class": "form-control"}),
        "otherName":forms.TextInput(attrs={"class": "form-control"}),
        "phoneNumber":forms.TextInput(attrs={"class": "form-control"}),
        "adminId":forms.TextInput(attrs={"class": "form-control"}),
    }