# Generated by Django 4.1.2 on 2022-11-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_client_admin_email_client_admin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='admin_email',
            field=models.CharField(default='', max_length=55, verbose_name='Contact Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='admin_name',
            field=models.CharField(default='', max_length=35, verbose_name='Contact'),
        ),
    ]