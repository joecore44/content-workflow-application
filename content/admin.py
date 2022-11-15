from django.contrib import admin
from .models import Client, Staff, Post, User, CompanyProfile, StaffProfile

admin.site.register(Client)
admin.site.register(Staff)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(CompanyProfile)
admin.site.register(StaffProfile)
