# imports from django
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import user
# Custom import files
from .models import Order, Product, ThroughModel
from .forms import ProductForm, OrderForm

# Create your views here.

@login_required
def index(request):
    # success = 0
    # if request.GET['message']:
    #     success = 1
    # else:
    #     success = 0

    orders_list = Order.objects.filter(user=request.user).order_by('-created')
    pending_orders = Order.objects.filter(status='Pending')
    context = {
        'orders_list': orders_list,
        'pending_orders': pending_orders,
        # 'success': success,       
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def pending_order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        order.delete()
        # response = redirect('index')
        # response['Location'] += '?message=success'
        # return response
        return redirect('index')
    context = {
        'order': order,
    }
    return render(request, 'dashboard/pending_order_delete.html', context)


'''
Render all orders from recent to olders
'''
@login_required
def all_orders(request):
    all_orders = Order.objects.all().order_by('-created')
    return render(request, 'dashboard/all_orders.html', {'all_orders':all_orders})

'''
Render order details for employee
'''
@login_required
def order_detail(request, id):
    order = Order.objects.get(pk=id)
    products = ThroughModel.objects.filter(order=order.id)
    context = {
        'order': order,
        'products': products,
    }
    return render(request, "dashboard/order_detail.html", context)

@login_required
def new_order(request):

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
            message_successfull = "The order has been placed!"
            # return redirect('index')
        
        context = {
            'description': description,
            'products': products,
            'user': request.user,
            'quantities': quantities,
            'message_successfull': message_successfull

            }
    else:
        context = {
            'list_products': list_products,
        }

    return render(request, 'dashboard/new_order.html',context)



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
    '''
    Check if product in orders
    '''
    order = Order.objects.filter(products=product_id)    
    if order:
        delete_product = 0
    else:
        delete_product = 1
    '''
    get the product info from DB using the ORM
    '''
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {
        'product': product,
        'delete_product': delete_product,
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