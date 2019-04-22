from django.contrib import admin
from .models import Event, Year, Month, Day, Hour, Minute

# Register your models here.

admin.site.register(Event)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(Minute)
