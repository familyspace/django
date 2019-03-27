from authapp.forms import SignInForm, SignUpForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.translation import gettext_lazy as _


class SignInView(LoginView):
    title = _('Sign In')
    form_class = SignInForm
    template_name = 'authapp/signin.html'
    success_url = '/'


class SignUpView(CreateView):
    title = _('Sign Up')
    form_class = SignUpForm
    template_name = 'authapp/signup.html'
    success_url = '/auth/signin'

# TODO: Написать контроллер для редактирования профиля
