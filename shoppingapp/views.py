from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from authapp.models import User
from groupapp.models import Group, GroupUser
from shoppingapp.forms import PurchaseCreationForm, PurchaseEditForm
from shoppingapp.models import ShopingItem
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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

class purchasecreation_page(CreateView):
    model = ShopingItem
    template_name = 'shoppingapp/purchasecreation.html'
    form_class = PurchaseCreationForm

    def get_success_url(self):
        return reverse_lazy('shop:shoppinglist', kwargs={'group_pk': Group.objects.get(id=self.kwargs.get('group_pk')).pk})

    def get_context_data(self, *args, **kwargs):
        context = super(purchasecreation_page, self).get_context_data(**kwargs)
        context['group_pk'] = Group.objects.get(id=self.kwargs.get('group_pk')).pk
        return context

    def form_valid(self, PurchaseCreationForm, **kwargs):
        group_pk = Group.objects.get(id=self.kwargs.get('group_pk')).pk
        self.object = PurchaseCreationForm.save(commit=False)
        self.object.group = get_object_or_404(Group, pk=group_pk)
        self.object.save()
        PurchaseCreationForm.save_m2m()
        return super(purchasecreation_page, self).form_valid(PurchaseCreationForm)

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
    item.delete()
    return HttpResponseRedirect(reverse('shop:shoppinglist', args=[group_pk]))