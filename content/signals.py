from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Client, Staff, Post, ClientProfile, StaffProfile

@receiver(post_save, sender=Client)
def create_client(sender, instance, created, **kwargs):
    if created and instance.role == 'CLIENT':
        ClientProfile.objects.create(user=instance)

@receiver(post_save, sender=Staff)
def create_staff(sender, instance, created, **kwargs):
    if created and instance.role == 'STAFF':
        StaffProfile.objects.create(user=instance)
    
        