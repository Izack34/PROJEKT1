# Generated by Django 3.0.5 on 2020-04-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_message_m_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
