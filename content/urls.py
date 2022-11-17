from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_home, name='dashboard'),
    path('detail', views.client_post_detail, name='client-post-detail'),
    path('company/new', views.company_create, name='create-company'),
    path('company/<str:slug>', views.company_update, name='update-company'),
    path('company/<str:slug>/follow' , views.follow_company, name='follow-company'),
    path('company/<str:slug>/delete', views.company_delete, name='delete-company'),
    path('company/<str:slug>/posts', views.get_company_posts, name='company-posts'),
    path('company/<str:slug>/posts/new', views.create_post, name='post-create'),
    path('company/post/<str:slug>', views.get_company_post_detail, name='post-detail'),
]
