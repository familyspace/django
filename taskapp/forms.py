from django import forms
from taskapp.models import Task

class NewTaskForm(forms.ModelForm):
    class Meta:
            model = Task
            fields = ('title', 'user', 'description')

    def __init__(self, *args, **kwargs):
        super(NewTaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Что сделать?"
        self.fields['description'].widget.attrs['placeholder'] = "Комментарий"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input100'
            self.fields[field].label = ""


class TaskEditForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

    class Meta:
            model = Task
            fields = ('title', 'user', 'description', 'done')

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Что сделать?"
        self.fields['description'].widget.attrs['placeholder'] = "Комментарий"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input100'
            self.fields[field].label = ""