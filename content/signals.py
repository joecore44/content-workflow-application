from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Client, Staff, Post, PostRevision

# Create post revision when a post is created
@receiver(post_save, sender=Post)
def create_post_revision(sender, instance, created, **kwargs):
    if created:
        staff = Staff.objects.get(user=instance.staff.user)
        revision = 'Initial Post Creation V1'
        PostRevision.objects.create(post=instance, revision=revision, staff=staff)
