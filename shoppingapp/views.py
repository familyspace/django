from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from groupapp.models import Group
from shoppingapp.forms import PurchaseCreationForm, PurchaseEditForm
from shoppingapp.models import ShopingItem

@login_required
def view_group_purchases(request, group_pk):
    '''
    Просмотр списка покупок группы по pk группы
    '''
    donelist = ShopingItem.objects.filter(group=group_pk, done=True)
    tobuylist = ShopingItem.objects.filter(group=group_pk, done=False)

    content = {
        'done': donelist,
        'todo': tobuylist,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/shoppinglist.html', content)

@login_required
def purchasecreation_page(request, group_pk):
    '''
    Добавление покупки в группу
    '''
    if request.method == 'POST':
        form = PurchaseCreationForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            group = get_object_or_404(Group, pk=group_pk)
            response.group = group
            response.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('shop:shoppinglist', args = [group_pk]))
    else:
        form = PurchaseCreationForm()

    content = {
        'purchase_form': form,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/purchasecreation.html', content)

@transaction.atomic
def purchase_edit(request, group_pk, title):
    '''
    Просмотр/изменение покупки группы
    '''
    purchase = get_object_or_404(ShopingItem, title=title)
    form = PurchaseEditForm(request.POST, instance=purchase)
    if purchase.title == title:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))
        else:
            form = PurchaseEditForm(instance=purchase)

    content = {
        'edit_form': form,
        'group_pk': group_pk,
        'title': title,
    }

    return render(request, 'shoppingapp/purchasedetails.html', content)

@login_required
def removeitem(request, title, group_pk):
    '''
    Удаление покупки
    '''
    item = get_object_or_404(ShopingItem, title=title)
    item.delete()
    return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))