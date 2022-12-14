# Generated by Django 4.1.2 on 2022-11-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_postcomment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('pending customer approval', 'Pending Customer Approval'), ('published', 'Published'), ('in design', 'In Design'), ('draft', 'Draft'), ('approved', 'Approved')], default='draft', max_length=50),
        ),
    ]
