from django.contrib import admin

from menu_app.models import Dish, Cart, CartItem, Order, OrderItem, Reviews

admin.site.register(Dish)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reviews)