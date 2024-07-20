from django.urls import path
from . import views

print("Loading order urls")
urlpatterns = [
    path("",views.index,name = "index"),
    path("orders/",views.orders_list,name='orders_list'),
]