from django import forms
from chatapp.models import Chat

class chatform(forms.ModelForm):
    class Meta:
            model = Chat
            fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(chatform, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = "Напишите сообщение"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""