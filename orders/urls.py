from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.order, name="order"),
    path("direccion/", views.address, name="address")
]