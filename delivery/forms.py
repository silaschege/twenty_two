from django import forms
from .models import DeliveryMode,Ontransit

class AddDeliveryModeForm(forms.ModelForm):
    class Meta:
        model = DeliveryMode
        fields=[
            "number_plate","make","type","color","carrying_weight","carrying_weight_metric" ,"carrying_size",
                ]
        labels={
                "number_plate":"Number Plate",
                "make":"Make",
                "type":"Type",
                "color":"Color",
                "carrying_weight":"Carrying Weight",
                "carrying_weight_metric":"Carrying Weight Metric" ,
                "carrying_size": "Carrying Size",
        }
        widgets={
                "number_plate":forms.TextInput(attrs={'class': 'form-control'}),
                "make":forms.TextInput(attrs={'class': 'form-control'}),
                "type":forms.TextInput(attrs={'class': 'form-control'}),
                "color":forms.TextInput(attrs={'class': 'form-control'}),
                "carrying_weight":forms.NumberInput(attrs={'class':'form-control'}),
                "carrying_weight_metric":forms.TextInput(attrs={'class': 'form-control'}),
                "carrying_size":forms.NumberInput(attrs={'class':'form-control'}),

        }

class onTransitForm(forms.ModelForm):
    class Meta:
        model = Ontransit
        fields = ["orderNumber","deliveryMode","captain",]
        labels = {"orderNumber":"Order Number",
                  "deliveryMode":"Delivery Mode",
                  "captain":"Captian",
                  }
        widgets = {
                    "orderNumber":forms.Select(attrs={'class':'form-control'}),
                    "deliveryMode":forms.Select(attrs={'class':'form-control'}),
                    "captain":forms.Select(attrs={'class':'form-control'}),
                    }