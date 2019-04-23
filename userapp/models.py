from django.db import models

#from authapp.models import User
from family_space import settings


class UserContactList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='Пользователь',
                             db_index=True,
                             on_delete='CASCADE',
                             related_name='contacts')
    contact_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name='Контакт пользователя',
                                     on_delete='CASCADE')

    def __str__(self):
        return self.contact_user.username + ' является другом ' + self.user.username
