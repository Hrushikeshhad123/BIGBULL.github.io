from django.contrib import admin
from . models import Products,Customer,Cart
# Register your models here.
@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title' ,'prod_img','category','desc']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user' , 'product','quantity']