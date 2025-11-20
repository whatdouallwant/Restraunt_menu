from django.shortcuts import render

from menu_app.models import Dish

def home(request):
    dishes = Dish.objects.all()

    return render(request, "menu/home.html", {
        "dishes": dishes,
    })
