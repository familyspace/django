from django.contrib import admin
from .models import Event, Hour, Minute, Day, Month, Year

# Register your models here.

admin.site.register(Event)
admin.site.register(Hour)
admin.site.register(Minute)
admin.site.register(Day)
admin.site.register(Month)
admin.site.register(Year)

