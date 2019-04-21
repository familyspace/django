from django.contrib import admin
from authapp.models import User, UserProfile, UserContactList

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserContactList)
