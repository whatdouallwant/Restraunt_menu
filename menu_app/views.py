from django.shortcuts import redirect, render

from menu_app.models import Dish, CartItem

def home(request):
    dishes = Dish.objects.all()

    return render(request, "menu/home.html", {
        "dishes": dishes,
    })

def cart(request):
    cart_items = CartItem.objects.all()

    return render(request, "menu/cart.html", {
        "cart_items": cart_items,
    })

def dish_detail(request, dish_id):
    dish = Dish.objects.get(id=dish_id)

    return render(request, "menu/dish_info.html", {
        "dish": dish,
    })
