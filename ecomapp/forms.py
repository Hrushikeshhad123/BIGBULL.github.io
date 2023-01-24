from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from . models import Customer                                                             

class CustomerProfileForm(forms . ModelForm):
    class meta:
        model =Customer
        fields = ['id','user','name','locality','city','zipcode']
    
        widgets = {
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'locality': forms.TextInput(attrs={'class' : 'form-control'}),
            'city' :forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile':forms.NumberInput(attrs={'class' : 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class' : 'form-control'}),
        }




class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={ 'class': 'form-control'}))
    password1= forms.CharField(widget = forms.PasswordInput(attrs={ 'class': 'form-control'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))
   
    class meta:
        model:User
        fields = ['username','email','password1','password2']

class LoginForm (AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={ 'class': 'form-control'}))

class CustomerProfileForm(forms . ModelForm):
    class meta:
        model =Customer
        fields = ['id','user','name','locality','city','zipcode']
        widgets = {
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'locality': forms.TextInput(attrs={'class' : 'form-control'}),
            'city' :forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile':forms.NumberInput(attrs={'class' : 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class' : 'form-control'}),
        }




class MyPasswordResetForm(PasswordChangeForm):
    pass
