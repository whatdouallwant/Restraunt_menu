from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu_app.models import Dish, CartItem, Cart, Order, Reviews, User
from .forms import ReviewForm

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
    dish = get_object_or_404(Dish, id=dish_id)

    reviews = (
        Reviews.objects
        .filter(dish=dish)
        .select_related('user')
        .order_by('-created_at')
    )

    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    form = ReviewForm() if request.user.is_authenticated and not user_review else None

    return render(request, "menu/dish_info.html", {
        "dish": dish,
        "reviews": reviews,    
        "form": form,
        "user_review": user_review,
    })

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def delete_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
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

def filter_by_category(request, category):
    dishes = Dish.objects.filter(category=category)

    return render(request, "menu/home.html", {
        "dishes": dishes,
    })

@login_required
def add_review(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    if Reviews.objects.filter(dish=dish, user=request.user).exists():
        return redirect('dish_detail', dish_id=dish.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.dish = dish
            review.save()

    return redirect('dish_detail', dish_id=dish.id)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)

    if request.user == review.user:
        review.delete()

    return redirect('dish_detail', dish_id=review.dish.id)

def order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    

    total_price = sum(item.dish.price * item.quantity for item in cart_items)
    payment = request.POST.get('payment')
    address = request.POST.get('address')

    cart_items.delete()

    return render(request, "menu/order.html", {
        "total_price": total_price,
    })