from django.db import models
from django.contrib.auth.models import User
    

class Dish(models.Model):
    CATEGORIES = [ 
        ('soup', 'Супи'),
        ('salad', 'Салати'),
        ('main_course', 'Основні блюда'),
        ('dessert', 'Десерти'),
        ('beverage', 'Напої'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    simelions = models.PositiveIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to="dishes_photos/", blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    ingredients = models.TextField(blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveBigIntegerField(default=0)
    available = models.BooleanField(default=True)

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
    TYPE = [
        ('cash', 'Готівка'),
        ('card', 'Карта'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="new")
    address = models.CharField(max_length=250, blank=True, null=True)
    payment = models.CharField(max_length=100, blank=True, null=True, choices=TYPE)


    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=200)
    dish_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

class Reviews(models.Model):
    RATING = [
        (1, '1 - Дуже погано'),
        (2, '2 - Погано'),
        (3, '3 - Задовільно'),
        (4, '4 - Добре'),
        (5, '5 - Відмінно'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.dish.name}"