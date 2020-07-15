from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import BillingProfile
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

# Create your views here.


class BillingProfileListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name ="billing_profiles/billing_profiles.html"

    def get_queryset(self):
        return self.request.user.billing_profiles


@login_required(login_url="login")
def create(request):

    if request.method == 'POST':
        if request.POST.get("stripeToken"):
            if not request.user.has_customer():
                request.user.create_customer_id()

            token = request.POST['stripeToken']
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user,token)

            if billing_profile:
                messages.success(request, "Tarjeta creada exitosamente")

    return render(request, "billing_profiles/create.html", {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })
