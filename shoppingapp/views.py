from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import models
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from authapp.models import User
from groupapp.models import Group, GroupUser
from shoppingapp.forms import PurchaseCreationForm, PurchaseEditForm
from shoppingapp.models import ShopingItem
from userapp.models import UserContactList
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


def check_credentials(groups, users):
    friendlyuser = GroupUser.objects.filter(group=groups, user=users)
    if not friendlyuser:
        return HttpResponseForbidden()

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

# class purchasecreation_page(CreateView):
#     model = ShopingItem
#     template_name = 'shoppingapp/purchasecreation.html'
#     # success_url = reverse_lazy( 'shop:shoppinglist' )
#     fields = ('title', 'user', 'price', 'comment')
#     # pk_url_kwarg = 'group_pk'
#
#     def get_success_url(self):
#         return reverse_lazy('shop:shoppinglist', kwargs={'pk': self.object['group_pk']})
#
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(purchasecreation_page, self).get_context_data(**kwargs)
#         # context['group_pk'] = self.group_pk
#         # args = [self.kwargs['group_pk']]
#         context['group_pk'] = Group.objects.get(id=self.kwargs['group_pk'])
#         return context

    # def form_valid(self, PurchaseCreationForm):
    #     PurchaseCreationForm.instance.group = get_object_or_404(Group, pk=group_pk)
    #     return super(purchasecreation_page, self).form_valid(PurchaseCreationForm)



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
def purchase_edit(request, group_pk, title):
    '''
    Просмотр/изменение покупки группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    purchase = get_object_or_404(ShopingItem, title=title)
    form = PurchaseEditForm(request.POST, instance=purchase)
    if purchase.title == title:
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
        'title': title,
    }

    return render(request, 'shoppingapp/purchasedetails.html', content)

@login_required
def removeitem(request, title, group_pk):
    '''
    Удаление покупки
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    item = get_object_or_404(ShopingItem, title=title)
    item.delete()
    return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))