from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile, Staff, Post

class ClientRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StaffRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'

class ClientUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ClientUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['admin_first_name', 'admin_last_name', 'admin_email', 'company_name', 'company_logo', 'phone', 'website' ]