# Generated by Django 5.0.2 on 2024-02-15 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_alter_product_options_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
    ]