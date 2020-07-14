from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.order, name="order"),
    path("direccion/", views.address, name="address"),
    path("seleccionar/direccion/", views.select_address, name="select_address"),
    path("establecer/direccion/<int:pk>/", views.check_address, name="check_address"),
    path("confirmacion/", views.confirm, name="confirm"),
    path("cancelar/", views.cancel, name="cancel")
]