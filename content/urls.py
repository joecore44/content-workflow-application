from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_home, name='dashboard'),
    path('company/new', views.company_create, name='create-company'),
    path('company/<str:slug>', views.company_update, name='update-company'),
    path('company/<str:slug>/follow' , views.follow_company, name='follow-company'),
    path('company/<str:slug>/delete', views.company_delete, name='delete-company'),
    path('company/<str:slug>/posts', views.get_company_posts, name='company-posts'),
    path('company/<str:slug>/posts/new', views.create_post, name='post-create'),
    path('company/post/<str:slug>/update', views.post_update, name='post-update'),
    path('company/post/<str:slug>/update/<int:image>', views.post_update, name='post-update'),
    path('company/post/<str:slug>', views.get_company_post_detail, name='post-detail'),
    path('company/post/<str:slug>/timeline', views.post_timeline, name='post-timeline'),
    path('company/post/<str:slug>/<int:image>', views.get_company_post_detail, name='post-detail'),
]
