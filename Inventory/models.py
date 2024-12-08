from django.db import models
from Authentication.models import User

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    code = models.CharField(max_length=64,unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64,unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    MRP = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True,null=True, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True , null = True)

    def __str__(self):
        return f'{self.name} ({self.code})'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)

    def update_total_price(self):
        self.total_price = self.quantity * self.product.price
        self.save()
        return self.total_price
    
    def __str__(self):
        return  f'{self.user.username}-{self.product.name}({self.quantity})'
