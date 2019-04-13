from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings
import userapp.views as userapp

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('userapp.urls', namespace='userapp')),
                  path('group/', include('groupapp.urls', namespace='groupapp')),
                  path('authapi/', include('api.apiauthapp.urls')),
                  path('userapi/', include('api.apiuserapp.urls')),
                  # path('groupapi/', include('api.apigroupapp.urls')),
                  path('docs/', include('api.apidocs.urls')),
                  path('auth/', include('authapp.urls', namespace='auth')),
                  path('group/<group_pk>/shopping/', include('shoppingapp.urls', namespace='shop'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
