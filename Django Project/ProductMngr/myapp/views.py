from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product_mst,Product_sub_cat

# Create your views here.
def products(request):
    products=Product_mst.objects.all().prefetch_related('product_sub_cat_set')
    return render(request,'index.html',{'products': products})
