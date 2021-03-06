# Generated by Django 3.1 on 2020-08-21 17:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('userType', models.CharField(max_length=200)),
                ('scheduledInterviews', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=2), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('participants', models.ManyToManyField(to='myportal.UserDetails')),
            ],
        ),
    ]
