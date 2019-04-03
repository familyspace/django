from django.urls import path
from authapp.views import SignInView, SignUpView, SignOutView, VerifyView, UserUpdateView

app_name = 'authapp'
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/<pk>/', UserUpdateView.as_view(), name='edit'),
    path('verify/', VerifyView.as_view(), name='verify'),
]