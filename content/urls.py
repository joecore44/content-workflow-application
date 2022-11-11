from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_home, name='dashboard'),
    path('detail', views.client_post_detail, name='client-post-detail'),
    path('add-client', views.add_client, name='add-client'),
    path('client-profile/<int:pk>/', views.client_profile, name='client-profile'),
]
