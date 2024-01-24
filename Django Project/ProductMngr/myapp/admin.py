from django.contrib import admin
from .models import Product_mst,Product_sub_cat

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['product','price','image','model','ram']

admin.site.register(Product_mst)
admin.site.register(Product_sub_cat,ProductAdmin)