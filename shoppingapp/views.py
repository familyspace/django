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

    list = ShopingItem.objects.filter(group=group_pk)

    content = {
        'purchases': list,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/shoppinglist.html', content)

@login_required
def purchasecreation_page(request, group_pk):
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

        group_pk = group_pk

    content = {
        'purchase_form': form,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/purchasecreation.html', content)

# @login_required
# def purchase_details(request, title):
#     # details = ShopingItem.objects.filter(title=title)
#     details = get_object_or_404(ShopingItem, title=title)
#     # grouppk = group_pk
#     content = {
#         'purchase_details': details,
#         # 'grpk': grouppk
#     }
#     return render(request, 'shoppingapp/purchasedetails.html', content)

@transaction.atomic
def purchase_edit(request, titles, group_pk, item_pk):
    purchase = ShopingItem.objects.filter(title=titles).first()
    # purchase = get_object_or_404(ShopingItem, title=titles)
    print(purchase)
    if request.method == 'POST':
        form = PurchaseEditForm(request.POST, instance=purchase)
        # purchase_edit_form = PurchaseEditForm(request.POST, request.FILES, instance=details)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))
    else:
        form = PurchaseEditForm(instance=purchase)

    content = {'edit_form': form}

    return render(request, 'shoppingapp/purchasedetails.html', content)

@login_required
def removeitem(request, title, group_pk):
    item = get_object_or_404(ShopingItem, title=title)
    item.delete()
    return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))