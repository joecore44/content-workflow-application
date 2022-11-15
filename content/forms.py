from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile, Staff, Post


class StaffRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [
          'status',
          'company_name',
          'company_logo',
          'phone',
          'admin_email',
          'website'
          ]
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
          'title',
          'content',
          'post_type',
          'deadline',
          'status',
          'image_1',
          'image_2',
          'image_3',
          'image_4',
          'image_5',
          'image_6',
          'image_7',
          'image_8',
          'image_9',
          'image_10',
          'video_file']