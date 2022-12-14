from django.db import models
from django.contrib.auth.models import User
import uuid

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField('CompanyProfile', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.company.company_name

class CompanyProfile(models.Model):
    COMPANY_CHOICES = (
        ('active', 'Active'),
        ('urgent', 'Urgent'),
        ('pending', 'Pending'),
    )   
    
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=COMPANY_CHOICES, default='active')
    admin_email = models.CharField(max_length=55,
    verbose_name='Contact Email', default='')
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='client-media/', blank=True)
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1, null=True)
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
    profile_image = models.ImageField(upload_to='staff-media/', default='staff-media/default.jpg')
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class CompanyFollowers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    company = models.ForeignKey('CompanyProfile', on_delete=models.CASCADE, related_name='followers')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' following ' + self.company.company_name

class Post(models.Model):
    STATUS_CHOICES = (
        ('pending customer approval', 'Pending Customer Approval'),
        ('published', 'Published'),
        ('in design', 'In Design'),
        ('draft', 'Draft'),
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
    client = models.ForeignKey(CompanyProfile, 
    on_delete=models.CASCADE, default='')
    staff = models.ForeignKey(Staff, 
    on_delete=models.CASCADE, null=True, 
    blank=True, default='')
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES, default='facebook_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
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
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1, null=True)
    
    def __str__(self):
        return self.title

class PostComment(models.Model):
    staff_comment = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' commenting on ' + self.post.title

class PostRevision(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    revision = models.TextField(null=False, verbose_name='Revision Notes')
    image = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff.user.first_name + ' | ' + self.revision