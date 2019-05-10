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
        self.fields['price'].widget.attrs['placeholder'] = "Цена"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input100'
            self.fields[field].label = ""


class PurchaseEditForm(forms.ModelForm):
    class Meta:
            model = ShopingItem
            fields = ('title', 'group', 'user', 'price', 'done', 'comment')

    def __init__(self, *args, **kwargs):
        super(PurchaseEditForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = "Комментарий"
        self.fields['price'].widget.attrs['placeholder'] = "Цена"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input100'
            self.fields[field].label = ""