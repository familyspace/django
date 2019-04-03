from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, SingleObjectMixin, FormMixin
from django.utils.translation import gettext_lazy as _

from authapp.forms import SignInForm, SignUpForm, UserUpdateForm, UserProfileUpdateForm
from authapp.models import User, UserProfile
from family_space import settings


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'authapp/signin.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'authapp/signup.html'
    success_url = '/auth/signin'


class SignOutView(LogoutView):
    title = _('Sign Out')


class UserUpdateView(UpdateView, FormMixin):
    model = User
    form_class = UserUpdateForm
    success_url = '/'
    template_name = 'authapp/update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Запрещаем править чужие профили
        if not request.user.is_authenticated or request.user.pk != self.object.pk:
            return HttpResponseForbidden()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        user = self.get_object()
        user_profile = UserProfile.objects.get(user__username=user.username)

        context['user_form'] = UserUpdateForm(initial=kwargs, instance=user)
        context['userprofile_form'] = UserProfileUpdateForm(initial=kwargs, instance=user_profile)

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        user_form = UserUpdateForm(request.POST, instance=request.user)
        userprofile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and userprofile_form.is_valid():
            user_form.save()

        return super().post(request, *args, **kwargs)


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
