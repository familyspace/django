from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.apishopingapp.views import ShopingViewSet, ShopingList

ShopingRouter = DefaultRouter()
ShopingRouter.register(r'shoping_api', ShopingViewSet, basename='shopingapi')

urlpatterns = [path('shoping_api/<int:group_id>/list/', ShopingList.as_view(), name='shopinglistapi'),
               ] + ShopingRouter.urls
