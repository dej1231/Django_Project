from email.policy import default
from django import forms
from .models import Product


# class RawProductForm(forms.Form):
#     name      = forms.CharField()
#     description = forms.CharField()
#     quantity      = forms.DecimalField()
#     price     = forms.DecimalField()
#     is_available     = forms.BooleanField(required=False)

class ProductForm(forms.ModelForm):
    name      = forms.CharField()
    description = forms.CharField()
    quantity      = forms.DecimalField()
    price     = forms.DecimalField()
    is_available     = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'price',
            'is_available'
        ]