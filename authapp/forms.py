from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

from authapp.models import User, UserProfile
from authapp.widgets import DateBSInput


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

    def save(self, commit=True):
        user = super(SignUpForm, self).save()
        user.get_activation_key()
        user.save()
        user.send_verify_email()

        return user


class UserUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = True
            field.widget.attrs['class'] = 'form-control'
            field.label = ""

            if field_name == 'username':
                field.widget.attrs['placeholder'] = _('Username')
            elif field_name == 'first_name':
                field.help_text = _('Your first name')
                field.widget.attrs['placeholder'] = _('First Name')
            elif field_name == 'last_name':
                field.help_text = _('Your last name')
                field.widget.attrs['placeholder'] = _('Last Name')
            elif field_name == 'phone':
                field.help_text = _('Your phone number')
                field.widget.attrs['placeholder'] = _('Phone number')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone')


class UserProfileUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = True
            field.label = ""

            if field_name == 'gender':
                field.help_text = _('Gender')

            elif field_name == 'birth_date':

                field.widget = DateBSInput()
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['required'] = True
                field.label = ""
                field.help_text = _('Your birth date')

    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date')
