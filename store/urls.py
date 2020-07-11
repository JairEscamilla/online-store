from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("usuarios/login/", views.login_view, name="login"),
    path("usuarios/logout/", views.logout_view, name="logout")
]
