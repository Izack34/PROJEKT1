# Generated by Django 3.0.3 on 2020-04-06 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Profile',
            new_name='profile',
        ),
    ]