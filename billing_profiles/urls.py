from django.urls import path
from . import views

app_name = "billing_profiles"
urlpatterns = [
    path("nuevo/", views.create, name="create"),
    path("", views.BillingProfileListView.as_view(), name="billing_profiles")
]