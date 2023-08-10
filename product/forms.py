from django import forms
from .models import ProductModel,ProductCategoryModel,ReceiveGoodsDetailHolderModel,ReceiveGoodsDetailModel


class AddProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryModel
        fields = ["product_category_name"]
        labels={
            "product_category_name":"Category Name",
           
        }
        widgets ={
            'product_category_name':forms.TextInput(attrs={'class':'form-control'}),
         
            
        }

class AddProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["product_category","product_name","product_description","packaging_quantity","product_image",]
        labels={
            "product_category":"Category",
            "product_name":"Name",
            "product_description":"Description",
            "packaging_quantity":"Packaging Quantity",
            "product_image":"Image",
        }
        widgets ={
            'product_category':forms.Select(attrs={'class':'form-control'}),
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_description':forms.TextInput(attrs={'class':'form-control'}),
            'packaging_quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'product_image':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            
        }


class SearchSupplierForm(forms.Form):
    searchSupplier = forms.CharField(
        label='Search Supplier',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class SearchProductForm(forms.Form):
    searchProduct = forms.CharField(
        label='Search Product',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class AddReceiveGoodsDetailForm(forms.ModelForm):
    class Meta:
        model = ReceiveGoodsDetailHolderModel
        fields = [
                "product",
                "buying_price",
                "quantity",
        ]
        labels={
                "product":"Product",
                "buying_price":"Buying Price",
                "quantity":"Quantity",
       
        }
        widgets ={
                "product":forms.Select(attrs={'class':'form-control'}),
                "buying_price":forms.NumberInput(attrs={'class':'form-control'}),
                "quantity":forms.NumberInput(attrs={'class':'form-control'}),
        }

class ProductPricingForm(forms.ModelForm):
    class Meta:
        model = ReceiveGoodsDetailModel
        fields = [
                "product",
                "buying_price",
                "quantity",
                "selling_price",
        ]
        labels={
                "product":"Product",
                "buying_price":"Buying Price",
                "quantity":"Quantity",
                "selling_price":"Selling Price",
       
        }
        widgets ={
                "product":forms.Select(attrs={'class':'form-control'}),
                "buying_price":forms.NumberInput(attrs={'class':'form-control'}),
                "quantity":forms.NumberInput(attrs={'class':'form-control'}),
                "selling_price":forms.NumberInput(attrs={'class':'form-control'}),
        }