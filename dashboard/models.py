from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
	('Pending','Pending'),
	('Approved','Approved'),
)

class PedidosUser(models.Model):
	email = models.EmailField('Email')
	user = models.CharField('User', max_length=50)
	passwd = models.CharField('Password', max_length=50)
	f_name = models.CharField('First Name', max_length=50)
	l_name = models.CharField('Last Name', max_length=50)
	b_day = models.DateTimeField('Birth Date')
	position = models.CharField('Position', max_length=50)
	def __str__(self):
		return self.f_name + ' ' + self.l_name


class Category(models.Model):
	category_name = models.CharField('Category', max_length=50)
	def __str__(self):
		return self.category_name


class Product(models.Model):
	product_name = models.CharField('Product Name', max_length=100)
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.product_name

class Order(models.Model):
	description = models.CharField('Order Description', max_length=100)
	status = models.CharField('Status', max_length=50, choices=STATUS)	
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	approval_date = models.DateTimeField('Approval Date', blank=True, null=True)
	def __str__(self):
		return self.description

