from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from authapp.models import User
from groupapp.models import Group, GroupUser
from shoppingapp.forms import PurchaseCreationForm, PurchaseEditForm
from shoppingapp.models import ShopingItem

@login_required
def view_group_purchases(request, group_pk):
    '''
    Просмотр списка покупок группы по pk группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    donelist = ShopingItem.objects.filter(group=group_pk, done=True)
    tobuylist = ShopingItem.objects.filter(group=group_pk, done=False)

    content = {
        'done': donelist,
        'todo': tobuylist,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/shoppinglist.html', content)

@login_required
def checkbox_shop_list(request, item_pk, group_pk):
    '''
    Функция меняет статут выполнено/невыполнено через чекбокс без захода на страницу редактирования
    '''

    if request.is_ajax():
        shop_item = ShopingItem.objects.get(pk=item_pk)
        if shop_item.done == False:
            shop_item.done = True
            shop_item.save()
        else:
            shop_item.done = False
            shop_item.save()

        donelist = ShopingItem.objects.filter(group=group_pk, done=True)
        tobuylist = ShopingItem.objects.filter(group=group_pk, done=False)

        content = {
            'done': donelist,
            'todo': tobuylist,
            'group_pk': group_pk
        }

        result = render_to_string('shoppingapp/includes/inc_shop_ajax.html', content)
        return JsonResponse({'result': result})
    else:
        return Http404

@login_required
def purchasecreation_page(request, group_pk):
    '''
    Добавление покупки в группу
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    form = PurchaseCreationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            response = form.save(commit=False)
            group = get_object_or_404(Group, pk=group_pk)
            response.group = group
            response.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('shop:shoppinglist', args = [group_pk]))
    else:
        formuser = User.objects.filter(pk__in=GroupUser.objects.filter(group=group_pk).values_list('user'))
        form = PurchaseCreationForm()
        form.fields['user'].queryset = formuser

    content = {
        'purchase_form': form,
        'group_pk': group_pk
    }

    return render(request, 'shoppingapp/purchasecreation.html', content)

@transaction.atomic
def purchase_edit(request, group_pk, item_pk):
    '''
    Просмотр/изменение покупки группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    purchase = get_object_or_404(ShopingItem, pk=item_pk)
    form = PurchaseEditForm(request.POST, instance=purchase)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))
    else:
        form = PurchaseEditForm(instance=purchase)
        formuser = User.objects.filter(pk__in=GroupUser.objects.filter(group=group_pk).values_list('user'))
        form.fields['user'].queryset = formuser

    content = {
        'edit_form': form,
        'group_pk': group_pk,
        'item_pk': item_pk,
    }

    return render(request, 'shoppingapp/purchasedetails.html', content)

@login_required
def removeitem(request, item_pk, group_pk):
    '''
    Удаление покупки
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    item = get_object_or_404(ShopingItem, pk=item_pk)
    print(item)
    item.delete()
    return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))





