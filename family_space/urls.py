from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings
import userapp.views as userapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls', namespace='auth')),
    path('userpage/', include('userapp.urls', namespace='userapp')),
    path('groupsapp/', include('groupapp.urls', namespace='groupapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

