from django.urls import path, include
import shoppingapp.views as shoppingapp


app_name = 'shoppingapp'
urlpatterns = [
    path('', shoppingapp.view_group_purchases, name='shoppinglist'),
    path('purchasecreation/', shoppingapp.purchasecreation_page, name='purchasecreation'),
    path('purchasedetails/<str:title>/', shoppingapp.purchase_edit, name='purchasedetails'),
    path('purchasedelete/<title>/', shoppingapp.removeitem, name='purchaseremove'),
]