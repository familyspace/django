from django import forms
from shoppingapp.models import ShopingItem

class PurchaseCreationForm(forms.ModelForm):
    class Meta:
            model = ShopingItem
            fields = ('title', 'user', 'price', 'comment')

    def __init__(self, *args, **kwargs):
        super(PurchaseCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Что купить"
        self.fields['comment'].widget.attrs['placeholder'] = "Комментарий"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""


class PurchaseEditForm(forms.ModelForm):
    class Meta:
            model = ShopingItem
            fields = ('title', 'group', 'done', 'price', 'comment', 'user')

    def __init__(self, *args, **kwargs):
        super(PurchaseEditForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = "Комментарий"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'logo-input'
            self.fields[field].label = ""