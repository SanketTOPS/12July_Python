from django import forms
from .models import Product_mst,Product_sub_cat

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_mst
        fields = ['product_name']

    price = forms.DecimalField(max_digits=10, decimal_places=2)
    image = forms.ImageField()
    model = forms.CharField(max_length=100)
    ram = forms.CharField(max_length=50)