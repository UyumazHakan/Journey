__author__ = 'Hakan Uyumaz'

import datetime

import pytz
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from ..utils import generate_token
from .work import Work
from .interest import Interest
from .education import Education


class UserManager(BaseUserManager):
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
    public_id = models.CharField('User Public ID', max_length=50)
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)

    summary = models.CharField('Summary', max_length=300, null=True, blank=True)

    profile_photo = models.ImageField(upload_to='uploaded/user_photos/%Y/%m/%d/%H/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='uploaded/cover_photos/%Y/%m/%d/%H/', null=True, blank=True)

    works = models.ManyToManyField(Work, related_name="users", null=True, blank=True)
    educations = models.ManyToManyField(Education, related_name="users", null=True, blank=True)
    interests = models.ManyToManyField(Interest, related_name="users", null=True, blank=True)

    activation_key = models.CharField(max_length=40, blank=True)
    activation_expire_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = UserManager()

    class Meta:
        pass

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.name

    def share_journey(self, journey):
        journey.sharers.add(self)

    def comment_journey(self, journey, text):
        from .comment import Comment

        comment = Comment(journey=journey, text=text, user=self)
        comment.save()
        del Comment

    def delete_comment(self, comment):
        if comment.user == self:
            comment.delete()

    def love_journey(self, journey):
        if journey.loves.filter(id=self.id):
            journey.loves.remove(self)
        else:
            journey.loves.add(self)

    def love_comment(self, comment):
        if comment.loves.filter(id=self.id):
            comment.loves.remove(self)
        else:
            comment.loves.add(self)