from django import forms
from .models import Farmer, Product

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['farmer', 'name', 'price', 'quantity', 'description']