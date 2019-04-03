from django.urls import path
from authapp.views import SignInView, SignUpView, SignOutView, VerifyView

app_name = 'authapp'
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('edit/', authapp.edit, name='edit'),
    # path('reset/', authapp.reset, name='reset'),
    path('verify/', VerifyView.as_view(), name='verify'),
]