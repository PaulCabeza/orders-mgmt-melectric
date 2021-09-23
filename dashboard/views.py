from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, Product
from .forms import ProductForm

# Create your views here.

def product_update(request, product_id):
    context = {

    }
    return render(request, 'dashboard/product_update.html', context)

def product_delete(request, product_id):
    # item = product_id
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {
        'product': product,
    }
    return render(request, 'dashboard/product_delete.html', context)

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
    # determine if sent to save the info or only render the blank form
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    context = {
        'products_list': products_list,
        'form': form,
    }
    return render(request, 'dashboard/products.html', context)

@login_required
def orders(request):
    # Render the orders on the DB
    orders_list = Order.objects.all()
    return render(request, 'dashboard/orders.html', {'orders_list':orders_list})