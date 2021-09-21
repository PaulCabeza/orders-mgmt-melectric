from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('products', views.products, name='products'),
    path('orders', views.orders, name='orders'),
]