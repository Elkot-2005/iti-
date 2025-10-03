from django.urls import path
from . import views
app_name = 'customers'
urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('detail/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('update/<int:pk>/', views.customer_update, name='customer_update'),
    path('delete/<int:pk>/', views.customer_delete, name='customer_delete'),
]
