# Generated by Django 3.0.4 on 2020-03-31 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_auto_20200331_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contract.Offer'),
        ),
    ]
