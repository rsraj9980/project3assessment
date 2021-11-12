from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList.as_view(), name='item_list'),
    path('items/create/', views.WishItemCreate.as_view(), name='item_create'),

]