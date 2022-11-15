from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "CLIENT", 'Client'
        STAFF = "STAFF", 'Staff'
        ADMIN = "ADMIN", 'Admin'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)

class Client(User):
    base_role = User.Role.CLIENT
    client = ClientManager()
    class Meta:
        proxy = True


class ClientProfile(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    company = models.OneToOneField('CompanyProfile', on_delete=models.CASCADE, null=True, blank=True)

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

class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STAFF)

class Staff(User):
    base_role = User.Role.STAFF
    class Meta:
        proxy = True
    staff = StaffManager()

    @property
    def profile(self):
        return self.staffprofile
    
    


class StaffProfile(models.Model):

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
    '''('pending customer review', 'Pending Customer Review'),
        ('pending customer revision', 'Pending Customer Revision'),
        ('published', 'Published'),
        ('in design', 'In Design'),'''
    
    STATUS_CHOICES = (
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
    staff = models.ForeignKey(StaffProfile, 
    on_delete=models.CASCADE, null=True, 
    blank=True, default='')
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
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1, null=True)
    
    def __str__(self):
        return self.title