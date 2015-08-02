# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='Email')),
                ('photo', models.ImageField(upload_to='uploaded/user_photos/%Y/%m/%d/%h/', blank=True, null=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('activation_expire_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.TextField(max_length=50)),
                ('cover_photo',
                 models.ImageField(upload_to='web/static/journey_photos/%Y/%m/%d/%h/', blank=True, null=True)),
                ('date', models.DateField()),
                ('summary', models.TextField(max_length=1000, blank=True, null=True)),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users',
                 models.ManyToManyField(related_name='users', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.TextField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=1000, blank=True, null=True)),
                ('journey', models.ForeignKey(to='base_communicator.Journey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
