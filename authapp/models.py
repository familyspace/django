from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.timezone import now
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    """
    Тематика группы
    """
    name = models.CharField(max_length=128,
                            blank=False,
                            )


class FSGroup(models.Model):
    """
    Группа
    name:
    is_private:
    category:
    get_all_users: возвращает  список всех пользователей группы
    """
    name = models.CharField(max_length=128,
                            blank=False,
                            )
    is_private = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    def get_all_users(self):
        users = FSAbstractUser.objects.filter(group__name=self.name)
        return users


class FSAbstractUser(AbstractUser):
    """
    Абстрактный Пользователь портала FamilySpace
    (Пользователь с минимальным набором аттрибутов, который может существовать на сервисе)
    username, first_name, last_name, email в родительском классе AbstractUser
    """

    activation_key = models.CharField(max_length=128, blank=True, editable=False)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)), editable=False)
    role = models.CharField(max_length=128, blank=True)
    group = models.ManyToManyField(FSGroup, on_delete=models.SET_NULL, default=None)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class FSUser(FSAbstractUser):
    """
    Пользователь портала (Сюда не должны входить пользователи обслуживающие сервис)
    Обязательные аттрибуты при регистрации
    gender: Пол
    birth_date: День рождения
    role: Роль в группе
    """

    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = ((MALE, 'M'),
                      (FEMALE, 'Ж'))

    gender = models.CharField(max_length='1',
                              blank=False,
                              choices=GENDER_CHOICES,
                              verbose_name=_('gender'),
                              )
    birth_date = models.DateField(verbose_name=_('birth_date'),
                                  blank=False)


class UserProfile(models.Model):
    """
    Профиль пользователя
    user:
    phone:
    get_all_groups: список всех групп пользователя
    """
    user = models.OneToOneField(FSUser,
                                unique=True,
                                null=False,
                                db_index=True,
                                on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=False, unique=True)

    def get_all_groups(self):
        groups = FSGroup.objects.filter(fsabstractuser__user=self.user)
        return groups

    @receiver(post_save, sender=FSUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=FSUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()