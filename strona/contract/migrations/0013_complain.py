# Generated by Django 3.0.5 on 2020-04-29 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0012_message_viewed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contract.Contract')),
            ],
        ),
    ]
