# Generated by Django 3.0.3 on 2020-04-21 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 11, 44, 13, 754372, tzinfo=utc)),
        ),
    ]
