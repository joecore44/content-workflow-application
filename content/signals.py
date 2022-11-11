from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Client, Staff, Post


@receiver(post_save, sender=Client)
def create_client(sender, instance, created, **kwargs):
    if created:
        client = Client.objects.filter(pk=instance.id).first()
        client.slug = client.company_name.replace(' ', '-')
        client.save()
        