from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings
import userapp.views as userapp


urlpatterns = [

    path('admin/', admin.site.urls),
    path('userapp/', userapp.usergroups_userapp, name='userpage'),
    path('', userapp.mainpage, name='mainpage'),
    path('login/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

