# from dashboard.views import products
from django import forms
from django.forms import fields
# from django.db.models import fields
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['description', 'products']

    products = forms.ModelMultipleChoiceField(
        queryset = Product.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )