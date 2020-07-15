from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required(login_url="login")
def create(request):

    print("Hola desde create")

    return render(request, "billing_profiles/create.html", {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })