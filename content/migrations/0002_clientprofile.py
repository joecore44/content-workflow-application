# Generated by Django 4.1.2 on 2022-11-13 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.companyprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='content.client')),
            ],
        ),
    ]