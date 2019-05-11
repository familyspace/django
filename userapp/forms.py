from django import forms
from groupapp.models import Group

class GroupCreationForm(forms.ModelForm):
    class Meta:
            model = Group
            fields = ('title', 'description', 'is_public', 'category')

    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Название группы"
        self.fields['description'].widget.attrs['placeholder'] = "Описание группы"
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['category'].label = 'Выберете категорию'
        self.fields['is_public'].label = ''

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input100'