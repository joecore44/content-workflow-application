from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='client-media/', blank=True)
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Staff(models.Model):
    DEPARTMENT_CHOICES = (
        ('sales', 'Sales'),
        ('marketing', 'Marketing'),
        ('operations', 'Operations'),
        ('development', 'Development'),
        ('management', 'Management'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='staff-media/', blank=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Post(models.Model):
    STATUS_CHOICES = (
        ('pending_customer_review', 'Pending Customer Review'),
        ('pending_customer_revision', 'Pending Customer Revision'),
        ('published', 'Published'),
        ('in_design', 'In Design'),
        ('approved', 'Approved'),
    )
    POST_TYPE_CHOICES = (
        ('blog', 'Blog'),
        ('video', 'Video'),
        ('facebook_image', 'Facebook Image Post'),
        ('facebook_carasel', 'Facebook Carasel Post'),
        ('instagram_image', 'Instagram Post'),
        ('instagram_reel', 'Instagram Reel'),
        ('instagram_story', 'Instagram Story Post'),
        ('linkedin_post', 'Linkedin Post'),
        ('twitter_post', 'Twitter Post'),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES, default='facebook_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')
    image_1 = models.ImageField(upload_to='post-media/', blank=True)
    image_2 = models.ImageField(upload_to='post-media/', blank=True)
    image_3 = models.ImageField(upload_to='post-media/', blank=True)
    image_4 = models.ImageField(upload_to='post-media/', blank=True)
    image_5 = models.ImageField(upload_to='post-media/', blank=True)
    image_6 = models.ImageField(upload_to='post-media/', blank=True)
    image_7 = models.ImageField(upload_to='post-media/', blank=True)
    image_8 = models.ImageField(upload_to='post-media/', blank=True)
    image_9 = models.ImageField(upload_to='post-media/', blank=True)
    image_10 = models.ImageField(upload_to='post-media/', blank=True)
    video_file = models.FileField(upload_to='post-media/', blank=True)
    
    def __str__(self):
        return self.title