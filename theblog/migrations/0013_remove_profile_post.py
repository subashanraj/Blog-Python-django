# Generated by Django 4.1.1 on 2022-10-21 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_profile_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
