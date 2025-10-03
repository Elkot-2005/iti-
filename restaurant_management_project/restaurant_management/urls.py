from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('menu/', include('menu.urls')),
    path('orders/', include('orders.urls')),
    path('customers/', include('customers.urls')),
]
