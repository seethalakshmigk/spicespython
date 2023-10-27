from unicodedata import name
from django.urls import path
from . import views
app_name='cart'


urlpatterns=[


    path('',views.cart_details,name="cart_details"),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('remove_cart/<int:product_id>/',views.cart_remove,name="cart_remove"),
    path('remove_full/<int:product_id>/', views.full_remove, name="full_remove"),

]
