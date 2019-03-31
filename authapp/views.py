from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _

from authapp.forms import SignInForm, SignUpForm
from authapp.models import User


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'authapp/signin.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'authapp/signup.html'
    success_url = '/auth/signin'


class SignOutView(LogoutView):
    title = _('Sign Out')


class VerifyView(TemplateView):
    template_name = 'authapp/verify.html'

    def get(self, request, *args, **kwargs):
        error_message = ''
        success_message = ''
        error_number = 0x00
        try:
            email = request.GET['email']
            activation_key = request.GET['activation_key']
            user = User.objects.get(email=email)

            if user.is_valid_activation_key(activation_key):
                user.activate()
                success_message = _('Activation is successful.')
            else:
                error_message = _('Error activation user.')
                error_number = 0x01

        except Exception as e:
            error_message = _('Error activation user: {}').format(e.args)
            error_number = 0x02

        self.extra_context = {'error_message': error_message,
                              'error_number': error_number,
                              'success_message': success_message, }
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

# TODO: Написать контроллер для редактирования профиля
