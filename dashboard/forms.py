# from dashboard.views import products
from django import forms
from django.forms import fields
from django.contrib import admin
# from django.db.models import fields
from .models import Category, Po, Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['description', 'products', 'user']

class PoForm(forms.ModelForm):
    class Meta:
        model = Po
        fields = ['po_number']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name',]


    # products = forms.ModelMultipleChoiceField(
    #     queryset = Product.objects.all(),
    #     widget = forms.CheckboxSelectMultiple,
    # )

    # products = forms.ModelMultipleChoiceField(
    #     Product.objects.all(),
    #     widget=admin.widgets.RelatedFieldWidgetWrapper(
    #         widget=admin.widgets.FilteredSelectMultiple('Products', False),
    #         rel=Order.products.rel,
    #         admin_site=admin.site
    #     ),
    #     required=False,
    # )