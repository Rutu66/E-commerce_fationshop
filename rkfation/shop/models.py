from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    
    class Meta:
        abstract=True
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

class Product(BaseModel):
    """ Product Object """
    
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True)
    name = models.CharField(_("Name"),max_length=255)
    price = models.IntegerField(_("Price"))
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Main Image"),upload_to="product_img")
    # image2 = models.ImageField(_("Inside1 Image"),upload_to="product_img")
    # image3 = models.ImageField(_("Inside2 Image"),upload_to="product_img")
    fabric = models.CharField(_("Fabric"),max_length=255)
    pattern = models.CharField(_("Pattern"),max_length=255)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering=("-created_at",)
        

class Category(BaseModel):
    """ Product Category object"""
    
    name = models.CharField(_("Product Category Name"),max_length=255)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering=("-created_at",)
        

class Cart(BaseModel):
    """ Cart object """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quantity"),default=1)
    
    def __str__(self) -> str:
        return self.product.name
    
    class Meta:
        ordering=("-created_at",)
        

class Address(BaseModel):
    """ address object """
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("Name"),max_length=255)
    mobile = models.IntegerField(_("Mobile"))
    address = models.CharField(_("Address"),max_length=255)
    city = models.CharField(_("City"),max_length=255)
    
    
    def __str__(self) -> str:
        return f"{self.name}, {self.mobile}, {self.address}, {self.city}"

    
    class Meta:
        ordering=("-created_at",)
        
class Order(BaseModel):
    """ Order object """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total = models.FloatField(_("Total"), default=1)
    
    def __str__(self) -> str:
        return self.user
    
    class Meta:
        ordering=("-created_at",)

        

    
    




