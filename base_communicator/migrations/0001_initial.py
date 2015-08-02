# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('public_id', models.CharField(max_length=50, verbose_name='User Public ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('profile_photo', models.ImageField(null=True, upload_to='uploaded/user_photos/%Y/%m/%d/%H/', blank=True)),
                ('cover_photo', models.ImageField(null=True, upload_to='uploaded/cover_photos/%Y/%m/%d/%H/', blank=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('activation_expire_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('program', models.TextField(max_length=50)),
                ('starting_date', models.DateField(null=True, verbose_name='Education Starting Date', blank=True)),
                ('ending_date', models.DateField(null=True, verbose_name='Education Ending Date', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Fr', 'Friend'), ('Fo', 'Follower')], max_length=50, verbose_name='Friendship Type')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Friendship Creation Date')),
                ('friend', models.ForeignKey(related_name='friendship_friend', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='friendship_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('D', 'Declined'), ('A', 'Accepted')], max_length=50, verbose_name='Status')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('cover_photo', models.ImageField(null=True, upload_to='web/static/journey_photos/%Y/%m/%d/%H/', blank=True)),
                ('date', models.DateField()),
                ('summary', models.TextField(null=True, max_length=1000, blank=True)),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='users')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField(null=True, max_length=1000, blank=True)),
                ('journey', models.ForeignKey(to='base_communicator.Journey')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('type', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('company', models.ForeignKey(related_name='company', to='base_communicator.Company')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(related_name='school', to='base_communicator.School'),
        ),
        migrations.AddField(
            model_name='user',
            name='educations',
            field=models.ManyToManyField(to='base_communicator.Education', related_name='educations'),
        ),
        migrations.AddField(
            model_name='user',
            name='works',
            field=models.ManyToManyField(to='base_communicator.Work', related_name='works'),
        ),
    ]
