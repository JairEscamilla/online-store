from django.contrib import admin
from django.urls import path, include
from . import views
from products.views import ProductListView
from products import urls

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path("usuarios/login/", views.login_view, name="login"),
    path("usuarios/logout/", views.logout_view, name="logout"),
    path("usuarios/registro/", views.register, name="register"),
    path("productos/", include("products.urls"))
]
