from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from authapp.models import User


class SignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = True
            field.widget.attrs['class'] = 'form-control'
            field.label = ""

            if field_name == 'username':
                field.widget.attrs['placeholder'] = _('Username')
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = _('Password')


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = True
            field.widget.attrs['class'] = 'form-control'
            field.label = ""

            if field_name == 'username':
                field.widget.attrs['placeholder'] = _('Username')
            elif field_name == 'email':
                field.help_text = _('Enter your email')
                field.widget.attrs['placeholder'] = _('Email')
            elif field_name == 'phone':
                field.help_text = _('Enter your phone number')
                field.widget.attrs['placeholder'] = _('Phone number')
            elif field_name == 'password1':
                field.widget.attrs['placeholder'] = _('Password')
            elif field_name == 'password2':
                field.widget.attrs['placeholder'] = _('Password again')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone')
