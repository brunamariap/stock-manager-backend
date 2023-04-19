from django import forms
from .models import Product, ProductSold


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'amount', 'unitary_value']


class ProductSoldModelForm(forms.ModelForm):
    class Meta:
        model = ProductSold
        fields = ['sold_amount']