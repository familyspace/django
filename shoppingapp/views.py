from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from shoppingapp.models import get_purchases_list, ShopingItem


# @login_required
# def view_all_purchases(request):
#     '''
#     Просмотр списка всех покупок
#     '''
#     list = get_purchases_list(request)
#
#     content = {
#         'purchases': list,
#     }
#
#     return render(request, 'shoppingapp/shoppinglist.html', content)

@login_required
def view_group_purchases(request, group_pk):
    '''
    Просмотр списка покупок группы по pk группы
    '''

    list = ShopingItem.objects.filter(group=group_pk)
    # list = map(lambda item: item.group, relations)
    # list = get_object_or_404(ShopingItem, pk=group_pk)
    # members = my_group.get_users()

    # relations = ShopingItem.objects.filter(user=user_pk)
    # list = map(lambda item: item.group, relations)

    content = {
        'purchases': list,
    }

    return render(request, 'shoppingapp/shoppinglist.html', content)
