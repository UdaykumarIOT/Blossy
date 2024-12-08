from django.db import models
from Authentication.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.JSONField(default=list , null=True , blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_method = models.CharField(max_length=10, choices=[('c', 'Cash'), ('o', 'Online')], default='c' , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)