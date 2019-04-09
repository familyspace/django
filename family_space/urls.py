from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings
import userapp.views as userapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpage/', include('userapp.urls', namespace='userapp')),
    path('groupsapp/', include('groupapp.urls', namespace='groupapp')),
    path('api/auth/', include('api.apiauthapp.urls')),
    path('api/profile/', include('api.apiuserapp.urls')),
    path('docs/', include('api.apidocs.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('shoppingapp/', include('shoppingapp.urls', namespace='shop'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

