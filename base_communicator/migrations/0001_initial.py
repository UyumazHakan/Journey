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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('public_id', models.CharField(verbose_name='User Public ID', max_length=50)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('surname', models.CharField(verbose_name='Surname', max_length=50)),
                ('email', models.EmailField(verbose_name='Email', unique=True, max_length=255)),
                ('summary', models.CharField(null=True, max_length=300, blank=True, verbose_name='Summary')),
                ('profile_photo',
                 models.ImageField(null=True, upload_to='uploaded/user_photos/%Y/%m/%d/%H/', blank=True)),
                ('cover_photo',
                 models.ImageField(null=True, upload_to='uploaded/cover_photos/%Y/%m/%d/%H/', blank=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('activation_expire_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('program', models.TextField(max_length=50)),
                ('starting_date', models.DateField(null=True, blank=True, verbose_name='Education Starting Date')),
                ('ending_date', models.DateField(null=True, blank=True, verbose_name='Education Ending Date')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('type', models.CharField(verbose_name='Friendship Type', max_length=50,
                                          choices=[('Fr', 'Friend'), ('Fo', 'Follower')])),
                ('creation_date', models.DateField(verbose_name='Friendship Creation Date', auto_now_add=True)),
                ('friend', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friendship_friend')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friendship_owner')),
            ],
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('status', models.CharField(verbose_name='Status', max_length=50,
                                            choices=[('P', 'Pending'), ('D', 'Declined'), ('A', 'Accepted')])),
                ('date', models.DateField(verbose_name='Date', auto_now_add=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('cover_photo',
                 models.ImageField(null=True, upload_to='web/static/journey_photos/%Y/%m/%d/%h/', blank=True)),
                ('date', models.DateField()),
                ('summary', models.TextField(null=True, max_length=1000, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owner')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='users')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField(null=True, max_length=1000, blank=True)),
                ('journey', models.ForeignKey(to='base_communicator.Journey')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('type', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('company', models.ForeignKey(to='base_communicator.Company', related_name='company')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(to='base_communicator.School', related_name='school'),
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
