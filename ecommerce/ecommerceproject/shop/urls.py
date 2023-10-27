from unicodedata import name
from django.urls import path
from . import views
app_name='shop'


urlpatterns = [

    path('', views.allproductcat,name="allpcat"),

    path('<slug:c_slug>/',views.allproductcat,name="product_by_cat"),

    path('<slug:c_slug>/<slug:product_slug>/', views.pro_detail, name="product_cat_detail"),

]
