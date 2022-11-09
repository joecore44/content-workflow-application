# Generated by Django 4.1.2 on 2022-11-09 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(blank=True, upload_to='client-media/')),
                ('phone', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to='staff-media/')),
                ('department', models.CharField(choices=[('sales', 'Sales'), ('marketing', 'Marketing'), ('operations', 'Operations'), ('development', 'Development'), ('management', 'Management')], max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post_type', models.CharField(choices=[('blog', 'Blog'), ('video', 'Video'), ('facebook_image', 'Facebook Image Post'), ('facebook_carasel', 'Facebook Carasel Post'), ('instagram_image', 'Instagram Post'), ('instagram_reel', 'Instagram Reel'), ('instagram_story', 'Instagram Story Post'), ('linkedin_post', 'Linkedin Post'), ('twitter_post', 'Twitter Post')], default='facebook_post', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending_customer_review', 'Pending Customer Review'), ('published', 'Published'), ('in_design', 'In Design')], default='draft', max_length=25)),
                ('image_1', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_2', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_3', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_4', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_5', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_6', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_7', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_8', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_9', models.ImageField(blank=True, upload_to='post-media/')),
                ('image_10', models.ImageField(blank=True, upload_to='post-media/')),
                ('video_file', models.FileField(blank=True, upload_to='post-media/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.client')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.staff')),
            ],
        ),
    ]
