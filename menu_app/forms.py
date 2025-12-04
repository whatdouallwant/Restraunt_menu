from django import forms
from .models import Reviews, Dish, Order, CartItem, OrderItem, User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        user = User
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }