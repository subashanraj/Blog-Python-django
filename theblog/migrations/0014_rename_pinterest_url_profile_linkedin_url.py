# Generated by Django 4.1.1 on 2022-10-21 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_remove_profile_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pinterest_url',
            new_name='linkedin_url',
        ),
    ]