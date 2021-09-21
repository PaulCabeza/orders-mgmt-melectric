from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, Product

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html', {})

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html', {})

@login_required
def products(request):
    # render all products from the DB
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
    }
    return render(request, 'dashboard/products.html', context)

@login_required
def orders(request):
    # Render the orders on the DB
    orders_list = Order.objects.all()
    return render(request, 'dashboard/orders.html', {'orders_list':orders_list})