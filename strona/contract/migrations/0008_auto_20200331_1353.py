# Generated by Django 3.0.4 on 2020-03-31 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
        ('contract', '0007_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Post'),
        ),
    ]
