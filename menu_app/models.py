from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    CATEGORIES = [ 
        ('soup', 'Супи'),
        ('salad', 'Салати'),
        ('main_course', 'Основные блюда'),
        ('dessert', 'Десерти'),
        ('beverage', 'Напої'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORIES, unique=True)

    def __str__(self):
        return self.name
    

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="static/", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id} of {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total for item in self.items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.quantity * self.dish.price
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="new") 

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=200)
    dish_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)