# Generated by Django 2.2.12 on 2024-03-12 14:14

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('mobile', models.IntegerField(verbose_name='Mobile')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('address_type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office')], max_length=20, verbose_name='Address type')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product Category Name')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='product_img', verbose_name='Main Image')),
                ('fabric', models.CharField(max_length=255, verbose_name='Fabric')),
                ('pattern', models.CharField(max_length=255, verbose_name='Pattern')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
