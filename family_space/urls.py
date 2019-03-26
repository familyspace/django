from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings


urlpatterns = [
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

