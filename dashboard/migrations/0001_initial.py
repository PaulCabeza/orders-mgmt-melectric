# Generated by Django 3.2.6 on 2021-09-14 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='PedidosUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('user', models.CharField(max_length=50, verbose_name='User')),
                ('passwd', models.CharField(max_length=50, verbose_name='Password')),
                ('f_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('b_day', models.DateTimeField(verbose_name='Birth Date')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Order Description')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('approval_date', models.DateTimeField(verbose_name='Approval Date')),
                ('products', models.ManyToManyField(blank=True, to='dashboard.Products')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.pedidosuser')),
            ],
        ),
    ]