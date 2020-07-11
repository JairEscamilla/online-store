from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product") #id -> Llave primaria
]