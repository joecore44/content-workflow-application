from django.contrib import admin
from .models import Client, Staff, Post 
from .models import CompanyProfile, CompanyFollowers, PostComment

admin.site.register(Client)
admin.site.register(Staff)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(CompanyProfile)
admin.site.register(CompanyFollowers)
