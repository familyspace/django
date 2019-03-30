from django.urls import path
from authapp.views import SignInView, SignUpView, verify

app_name = 'authapp'
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    # path('logout', authapp.logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('edit/', authapp.edit, name='edit'),
    # path('reset/', authapp.reset, name='reset'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]