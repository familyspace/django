from django import forms
from taskapp.models import Task

class NewTaskForm(forms.ModelForm):
    class Meta:
            model = Task
            fields = ('title', 'user')

    def __init__(self, *args, **kwargs):
        super(NewTaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Что сделать?"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""


class TaskEditForm(forms.ModelForm):
    class Meta:
            model = Task
            fields = ('title', 'user', 'done')

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Что сделать?"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""