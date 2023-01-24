from django.shortcuts import redirect,render
from django.http import HttpResponse
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm,MyPasswordResetForm



urlpatterns= [
    path ('',views.index, name = 'index'),

    path ('about/',views.about, name = 'about'),
    path ('contact/',views.contact, name = 'contact'),
    path("category/<slug:val>" ,views.CategoryView.as_view(), name  = "category"),
    path("categorytitle/<val>" ,views.Categorytitle.as_view(), name  = "title"),
    path("product_detailes/<int:pk>" , views.product_detailes.as_view(), name  = "product_detailes"),
    path("CustomerRegistrationView/",views.CustomerRegistrationView.as_view(), name  = "customerregistration"),
    path('accounts/login/' ,auth_view.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm) ,name = 'login'),
    path('password-reset/' ,auth_view.PasswordResetView.as_view(template_name = 'password_reset.html', form_class =MyPasswordResetForm) ,name = 'password_reset'),
    path('profile/',views.ProfileView.as_view(), name = 'profile'),
    path('logout/',auth_view.LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('add-to-cart/',views.add_to_cart, name = "add-to-cart"),
    path('Cart/',views.show_Cart, name = "showCart"),
    
    



    

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)