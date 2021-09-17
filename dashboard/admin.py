from django.contrib import admin
from .models import Category
from .models import PedidosUser
from .models import Products
from .models import Orders

# Register your models here.

admin.site.site_header = 'M-Electric Materials Orders App'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('description', 'status')

admin.site.register(Category)
admin.site.register(PedidosUser)
admin.site.register(Products)
admin.site.register(Orders, OrderAdmin)