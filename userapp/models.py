from django.db import models
from authapp.models import FamilyUser


# Create your models here.

class UserContactList(models.Model):
    user = models.ForeignKey(FamilyUser,
                             verbose_name='Пользователь',
                             db_index=True,
                             on_delete='CASCADE',
                             related_name='contacts')
    contact_user = models.ForeignKey(FamilyUser,
                                     verbose_name='Контакт пользователя',
                                     on_delete='CASCADE')
