from django.shortcuts import redirect, render

from menu_app.models import Dish, CartItem, Cart, Reviews, User

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

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.dish.price * item.quantity for item in cart_items)

    cart_items.delete()

    return render(request, "menu/order.html", {
        "total_price": total_price,
    })
