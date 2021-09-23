from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('products', views.products, name='products'),
    path('product-delete/<int:product_id>', views.product_delete, name='product-delete'),
    path('product-update', views.product_update, name='product-update'),
    path('orders', views.orders, name='orders'),
]