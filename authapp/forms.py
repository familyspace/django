from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import FamilyUser

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'logo-input',
        'placeholder':'Your login'
        }
    ))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={
        'class':'logo-input',
        'placeholder':'Your password'
        }
    ))

class RegistrationForm(UserCreationForm):
    class Meta:
        model = FamilyUser
        fields = ('username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'your nickname'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['email'].widget.attrs['placeholder'] = 'your email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'