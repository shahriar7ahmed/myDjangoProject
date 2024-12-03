from django.db import models
from django.contrib.auth.models import User  # Import Django's User model

# Create your models here.

class Item(models.Model): 
    title = models.CharField(max_length=200) 
    price = models.IntegerField() 
    discount = models.IntegerField() 
    slug = models.SlugField(unique=True) 
    
    def __str__(self): 
        return self.title  # Fixed self.user.title to self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed 'user' to User
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)  # Changed Ordered to ordered
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed 'user' to User
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)  # Changed Ordered to ordered
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username