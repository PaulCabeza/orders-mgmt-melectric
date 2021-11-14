from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('products', views.products, name='products'),
    path('product-delete/<int:product_id>', views.product_delete, name='product-delete'),
    path('product-update/<int:product_id>', views.product_update, name='product-update'),
    path('orders', views.index, name='orders'),
    path('new-order', views.new_order, name='new-order'),
    path('order-detail/<int:id>', views.order_detail, name='order-detail'),
    path('all-orders', views.all_orders, name='all-orders'),
    path('pending-order-delete/<int:order_id>', views.pending_order_delete, name='pending-order-delete'),
    path('review-order/<int:order_id>', views.review_order, name='review-order'),
    path('categories', views.categories, name='categories'),
]