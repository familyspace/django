from django.contrib import admin
from authapp.models import FSGroup, FSUser, FSAbstractUser, UserProfile, Category
# Register your models here.
admin.site.register(FSGroup)
admin.site.register(FSUser)
admin.site.register(FSAbstractUser)
admin.site.register(UserProfile)
admin.site.register(Category)