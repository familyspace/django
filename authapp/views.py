from authapp.forms import SignInForm
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _


class SignInView(LoginView):
    title = _("Sign in")
    form_class = SignInForm
    template_name = 'authapp/signin.html'


# TODO: Написать контроллер для регистрации пользователя

# TODO: Написать контроллер для регистрации пользователя
