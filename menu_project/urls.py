"""
URL configuration for menu_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from menu_app.views import home, cart_view, dish_detail, add_to_cart, order, filter_by_category, delete_from_cart, add_review, delete_review, order_view, admin_edit_order, order_view, orders_view, delete_order_for_admin, dish_edit_view, add_new_dish
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('cart/', cart_view, name='cart'),
    path('dish/<int:dish_id>/', dish_detail, name='dish_detail'),
    path('add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('order_view/', order_view, name='order'),
    path('category/<str:category>/', filter_by_category, name='filter_by_category'),
    path('delete_from_cart/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    path('add_review/<int:dish_id>/', add_review, name='add_review'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('admin_edit_order/<int:order_id>/', admin_edit_order, name='admin_orders_edit'),
    path('admin_orders/', orders_view, name='admin_orders'),
    path('delete_order_for_admin/<int:order_id>/', delete_order_for_admin, name='delete_order_for_admin'),
    path('dish_edit/<int:dish_id>/', dish_edit_view, name='dish_edit_view'),
    path('add_new_dish/', add_new_dish, name='add_new_dish'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)