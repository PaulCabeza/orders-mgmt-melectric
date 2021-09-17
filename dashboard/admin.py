from django.contrib import admin
from .models import Category
from .models import PedidosUser
from .models import Product
from .models import Order

# Register your models here.

admin.site.site_header = 'M-Electric Materials Orders App'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('description', 'status')
    list_filter = ('status',)

admin.site.register(Category)
admin.site.register(PedidosUser)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)