from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class SignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = True
            field.widget.attrs['class'] = "form-control"
            field.label = ""

            if field_name == 'username':
                field.widget.attrs['placeholder'] = _("Username")
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = _("Password")
