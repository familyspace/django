from django.urls import path
from authapp.views import SignInView

app_name = 'authapp'
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    # path('logout', authapp.logout, name='logout'),
    # path('register/', authapp.register, name='register'),
    # path('edit/', authapp.edit, name='edit'),
    # path('reset/', authapp.reset, name='reset'),
    # path('verify/<email>/<activation_key>/', authapp.verify, name='verify'),
]