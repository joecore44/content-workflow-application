# Generated by Django 4.1.2 on 2022-11-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='image',
            field=models.IntegerField(default=1),
        ),
    ]
