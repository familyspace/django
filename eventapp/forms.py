from django import forms
from .models import Event, Year, Month, Day, Hour, Minute


class EventCreationForm(forms.ModelForm):
    year_value = forms.ModelChoiceField(queryset=Year.objects.all(), initial='')
    month_value = forms.ModelChoiceField(queryset=Month.objects.all(), initial='')
    day_value = forms.ModelChoiceField(queryset=Day.objects.all(), initial='')
    hour_value = forms.ModelChoiceField(queryset=Hour.objects.all(), initial='')
    minute_value = forms.ModelChoiceField(queryset=Minute.objects.all(), initial='')

    class Meta:
            model = Event
            fields = ('title', 'description', 'location', 'date', 'year_value', 'month_value', 'day_value', 'hour_value', 'minute_value')

    def __init__(self, *args, **kwargs):
        super(EventCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Название события"
        self.fields['description'].widget.attrs['placeholder'] = "Описание события"
        self.fields['location'].widget.attrs['placeholder'] = "Место"
        self.fields['date'].widget.attrs['placeholder'] = "Время YYYY-mm-dd HH:MM"
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['location'].label = ''
        self.fields['date'].label = ''
        self.fields['year_value'].queryset = Year.objects.all()
        self.fields['month_value'].queryset = Month.objects.all()
        self.fields['day_value'].queryset = Day.objects.all()
        self.fields['hour_value'].queryset = Hour.objects.all()
        self.fields['minute_value'].queryset = Minute.objects.all()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'

class YearChooseForm(forms.Form):
    year_value = forms.ModelChoiceField(queryset=Year.objects.all(), initial='')
    month_value = forms.ModelChoiceField(queryset=Month.objects.all(), initial='')
    day_value = forms.ModelChoiceField(queryset=Day.objects.all(), initial='')

    def __init__(self, *args, **kwargs):
        super(YearChooseForm, self).__init__(*args, **kwargs)
        self.fields['year_value'].queryset = Year.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = ''
            field.help_text = ''