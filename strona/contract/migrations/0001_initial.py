# Generated by Django 3.0.4 on 2020-03-28 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_post_tags'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='users.Profile')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('deadline', models.DateField()),
                ('description', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='users.Profile')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executor', to='users.Profile')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contract.Offer')),
            ],
        ),
    ]