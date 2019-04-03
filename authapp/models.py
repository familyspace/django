import hashlib
import random

import jwt
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.utils.timezone import now
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from datetime import datetime, timedelta
import time

from family_space import settings


class User(AbstractUser):
    """
    Пользователь портала (расширение AbstractUser)

    Аттрибуты:
    activation_key:
    activation_key_expires:
    phone:

    Методы:
    is_activation_key_expired:

    """

    phone = models.CharField(max_length=20,
                             blank=True,
                             null=True,
                             unique=True,
                             verbose_name=_('Phone'))

    activation_key = models.CharField(max_length=128,
                                      blank=True,
                                      editable=False,
                                      verbose_name=_('Activation key'), )
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)),
                                                  editable=False,
                                                  verbose_name=_('Activation key expires'))

    @property
    def token(self):
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        dt_exp = time.mktime((datetime.now() + timedelta(days=settings.EXP_TOKEN)).timetuple())

        token = jwt.encode({
            'user_id': self.pk,
            'exp': int(dt_exp),
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True

    # Генерация кода активации
    def get_activation_key(self):
        self.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        self.activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()

    # Отправка пользователю письма с кодом активации
    def send_verify_email(self):
        email = EmailMessage()
        email.subject = _('Family Space Sign Up Confirmation')
        email.from_email = settings.EMAIL_HOST_USER
        email.to.append(self.email)
        verify_link = reverse(settings.EMAIL_VERIFY_VIEW)
        email.body = _(
            'Hello, {}! Сlick the link below to complete your registration\n {}{}?email={}&activation_key={}').format(
            self.username,
            settings.DOMAIN_NAME,
            verify_link,
            self.email,
            self.activation_key)
        return email.send()

    # Проверка кода активации
    def is_valid_activation_key(self, activation_key=None):
        if self.activation_key == activation_key and not self.is_activation_key_expired():
            return True
        else:
            return False

    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()
        self.save()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('FamilySpace user')
        verbose_name_plural = _('FamilySpace users')


class UserProfile(models.Model):
    """
    Профиль пользователя
    """
    user = models.OneToOneField(User,
                                unique=True,
                                null=False,
                                db_index=True,
                                on_delete=models.CASCADE,
                                verbose_name=_('User'))
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = ((MALE, _('M')),
                      (FEMALE, _('W')))

    gender = models.CharField(max_length=1,
                              blank=True,
                              choices=GENDER_CHOICES,
                              verbose_name=_('Gender'),
                              )
    birth_date = models.DateField(verbose_name=_('Birth date'),
                                  blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('Users profile')
