from django.shortcuts import render
# from django.http import HttpResponse
from .models import Order

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html', {})

def staff(request):
    return render(request, 'dashboard/staff.html', {})

def products(request):
    return render(request, 'dashboard/products.html', {})

def orders(request):
    # Render the orders on the DB
    orders_list = Order.objects.all()
    return render(request, 'dashboard/orders.html', {'orders_list':orders_list})