__author__ = 'Hakan Uyumaz'

import random
import datetime

import pytz
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from ..utils import generate_token


class Usermanager(BaseUserManager):
    def create_user(self, name=None, surname=None, email=None, password=None):
        if not (name and surname and password and email):
            raise ValueError('An user requires username, name, surname, email, password')

        user = self.model(
            name=name.title(),
            surname=surname.title(),
            email=self.normalize_email(email),
            activation_key=generate_token(),
            activation_expire_date=datetime.datetime.now(pytz.utc) + datetime.timedelta(2),
        )

        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name=None, surname=None, email=None, password=None):
        user = self.create_user(
            name=name,
            surname=surname,
            email=email,
            password=password
        )

        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):

    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)

    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True
    )

    photo = models.ImageField(upload_to='uploaded/user_photos/%Y/%m/%d/%h/', null=True, blank=True)

    activation_key = models.CharField(max_length=40, blank=True)
    activation_expire_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = Usermanager()

    class Meta:
        pass

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.name