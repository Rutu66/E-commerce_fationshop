from django.contrib import admin
from shop.models import*

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)


