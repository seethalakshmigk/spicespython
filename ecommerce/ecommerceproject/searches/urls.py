from unicodedata import name
from django.urls import path
from . import views
app_name='searches'

urlpatterns=[
    path('',views.search_result,name="srch"),
]