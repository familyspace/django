from django import forms
from groupapp.models import GroupUser

class RoleEdit(forms.ModelForm):
    class Meta:
            model = GroupUser
            fields = ('role',)

    def __init__(self, *args, **kwargs):
        super(RoleEdit, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""