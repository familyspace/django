from django.urls import path, include
import authapp.views as authapp


app_name = 'authurls'
urlpatterns = [
    path('', authapp.login, name='authlogin'),
    path('logout/', authapp.logout, name='authlogout'),
    path('registration/', authapp.registration, name='authreg'),
]
