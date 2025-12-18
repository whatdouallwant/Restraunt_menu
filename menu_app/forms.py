from django import forms
from .models import Reviews, Dish, Order, CartItem, OrderItem, User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }