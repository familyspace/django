from django.db import models

# Create your models here.
from authapp.models import User


class UserContactList(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             db_index=True,
                             on_delete='CASCADE',
                             related_name='contacts')
    contact_user = models.ForeignKey(User,
                                     verbose_name='Контакт пользователя',
                                     on_delete='CASCADE')

    def __str__(self):
        return self.contact_user.username + ' является другом ' + self.user.username