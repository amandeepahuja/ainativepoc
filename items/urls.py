from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/items/', views.item_list, name='item_list'),
    path('api/items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('api/items/create/', views.item_create, name='item_create'),
    path('api/items/<int:item_id>/update/', views.item_update, name='item_update'),
    path('api/items/<int:item_id>/delete/', views.item_delete, name='item_delete'),
    path('api/items/search/', views.item_search, name='item_search'),
] 