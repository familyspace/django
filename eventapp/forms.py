from django import forms
from .models import Event, Hour, Minute, Day, Month, Year


class EventForm(forms.Form):
    title = forms.CharField(label='Краткое описание события', max_length=32)
    description = forms.CharField(label='Описание события', widget=forms.Textarea)
    location = forms.CharField(label='Место', max_length=32)
    hour = forms.ModelChoiceField(queryset=Hour.objects.all())
    minute = forms.ModelChoiceField(queryset=Minute.objects.all())
    day = forms.ModelChoiceField(queryset=Day.objects.all())
    month = forms.ModelChoiceField(queryset=Month.objects.all())
    year = forms.ModelChoiceField(queryset=Year.objects.all())

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
        self.fields['hour'].widget.attrs['class'] = 'form-control'
        self.fields['minute'].widget.attrs['class'] = 'form-control'
        self.fields['day'].widget.attrs['class'] = 'form-control'
        self.fields['month'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['style'] = "height:120px"



