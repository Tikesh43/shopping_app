from cgitb import text
import datetime
from unicodedata import category
from django.db import models
from django.db.models.fields import related

# Create your models here.
class Users(models.Model):
    ROLE_CHOICES = (
        ('admin', 'ADMIN'),
        ('seller', 'SELLER'),
        ('user', 'USER'),
    )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"


# product details model here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name

class Product(models.Model):  
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField( max_digits=15, decimal_places=2)
    category = models.ForeignKey("category", on_delete=models.CASCADE, related_name="products")
    stock = models.PositiveIntegerField()
    available = models.BooleanField( default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

