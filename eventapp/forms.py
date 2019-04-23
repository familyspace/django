from django import forms
from .models import Event, Hour, Minute, Day, Month, Year


class EventCreationForm(forms.Form):
    title = forms.CharField(label='Краткое описание события', max_length=32)
    description = forms.CharField(label='Описание события', widget=forms.Textarea)
    location = forms.CharField(label='Место', max_length=32)
    hour = forms.ModelChoiceField(queryset=Hour.objects.all(), initial='')
    minute = forms.ModelChoiceField(queryset=Minute.objects.all(), initial='')
    day = forms.ModelChoiceField(queryset=Day.objects.all(), initial='')
    month = forms.ModelChoiceField(queryset=Month.objects.all(), initial='')
    year = forms.ModelChoiceField(queryset=Year.objects.all(), initial='')

    def __init__(self, *args, **kwargs):
        super(EventCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'

# class EventCreationForm(forms.ModelForm):
#     year_value = forms.ModelChoiceField(queryset=Year.objects.all(), initial='')
#     month_value = forms.ModelChoiceField(queryset=Month.objects.all(), initial='')
#     day_value = forms.ModelChoiceField(queryset=Day.objects.all(), initial='')
#     hour_value = forms.ModelChoiceField(queryset=Hour.objects.all(), initial='')
#     minute_value = forms.ModelChoiceField(queryset=Minute.objects.all(), initial='')
#
#     class Meta:
#             model = Event
#             fields = ('title', 'description', 'location', 'hour_value', 'minute_value', 'day_value', 'month_value', 'year_value')
#
#     def __init__(self, *args, **kwargs):
#         year_default = kwargs.pop('default_year', None)
#         super(EventCreationForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs['placeholder'] = "Название события"
#         self.fields['description'].widget.attrs['placeholder'] = "Описание события"
#         self.fields['location'].widget.attrs['placeholder'] = "Место"
#         # self.fields['date'].widget.attrs['placeholder'] = "Время YYYY-mm-dd HH:MM"
#         self.fields['title'].label = ''
#         self.fields['description'].label = ''
#         self.fields['location'].label = ''
#         self.fields['hour_value'].queryset = Hour.objects.all()
#         self.fields['minute_value'].queryset = Minute.objects.all()
#         self.fields['year_value'].queryset = Year.objects.all()
#         self.fields['month_value'].queryset = Month.objects.all()
#         self.fields['day_value'].queryset = Day.objects.all()
#
#         print('Форма инициализирована, ', year_default)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'logo-input'
#
#
