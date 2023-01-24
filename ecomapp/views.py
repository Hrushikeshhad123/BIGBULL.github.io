from django.shortcuts import render,redirect
from django.db.models import Count
from . import views
from urllib import request
from django.views import View
from . models import Products
from django.http import HttpResponse
from django import forms
from . forms import CustomRegistrationForm
from . forms import CustomerProfileForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, 'contact.html')


class CategoryView(View):
    def get(self,request,val):
        productss = Products.objects.filter(category = val)
        title = Products.objects.filter(category= val).values('title')
        return render(request, "category.html",locals())

class Categorytitle(View):
    def get(self,request,val):
        productss = Products.objects.filter(title= val)
        title = Products.objects.filter(category = productss[0].category).values('title')
        return render(request, "category.html",locals())

class product_detailes(View):
    def get(self,request,pk):
        productss = Products.objects.get(pk = pk)
        return render(request,"product_detail.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomRegistrationForm()
        return render(request,"customerregistration.html",locals())

    def post(self,request):
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'reg.html')
        else:
            messages.warning(request,"invalid input data")

        return render(request,"customerregistration.html",locals())


class ProfileView(View):
    def get(self,request):

        return render(request, 'profile.html',locals())
    def post(self,request):
      
        return render(request, 'profile.html', locals())

def add_to_cart(request):
   user = request.user
   prod_id = request.Get.get('prod_id')
   product = Products.object.get(id = prod_id)
   Cart(user = user,product = product).save()
   return redirect('/Cart')




def show_Cart(request):
    user = request.user
    cart  = Cart.objects.filter(user = user)
    return render(request, "addtocart.html", locals())
