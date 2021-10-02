# imports from django
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Custom import files
from .models import Order, Product
from .forms import ProductForm, OrderForm

# Create your views here.

@login_required
def prueba(request):

    list_products = Product.objects.all()
    
    if request.method == 'POST':
        description = request.POST['description']
        # get the list of products from html
        products = request.POST.getlist('products')
        quantities = request.POST.getlist('quantities')
        # create the order object to save a record
        order_form = Order()
        order_form.description = description
        order_form.status = 'Pending'   
        order_form.user = request.user
        order_form.save()
        # save m2m products in this order        
        for prod, quan in zip(products, quantities):
            order_form.products.add(prod, through_defaults={'quantity': quan})
        
        context = {
            'description': description,
            'products': products,
            'user': request.user,
            'quantities': quantities,

            }
    else:
        context = {
            'list_products': list_products,
        }

    return render(request, 'dashboard/pruebacustomsaveform.html',context)

@login_required
def new_order(request, user):
    if request.method == 'POST':
        form = OrderForm(request.POST)
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'dashboard/new_order.html', context)

@login_required
def index(request):
    orders_list = Order.objects.all()
    context = {
        'orders_list': orders_list,
    }
    return render(request, 'dashboard/index.html', context)

# render the staff page
@login_required 
def staff(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'dashboard/staff.html', context)

def product_update(request, product_id):
    # determine if receive data to render the product info to edit
    item = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid:
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=item)
    # creating the context dictionary ready to be sent to the view
    context = {
        'form': form
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def product_delete(request, product_id):
    # get the product info from DB using the ORM
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {
        'product': product,
    }
    return render(request, 'dashboard/product_delete.html', context)

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