# Generated by Django 4.1.2 on 2022-11-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_post_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.TextField(verbose_name='Revision Notes')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.post')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.staff')),
            ],
        ),
    ]
