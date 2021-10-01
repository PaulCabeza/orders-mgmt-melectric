# Generated by Django 3.2.6 on 2021-09-30 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Order Description')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], max_length=50, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True, verbose_name='Approval Date')),
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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='ThroughModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, through='dashboard.ThroughModel', to='dashboard.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
