from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('add-items/<int:pk>/', views.add_items, name='add_items'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
]
