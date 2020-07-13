from django.shortcuts import render
from django.views.generic import ListView
from .models import ShippingAddress
from .forms import ShippingAddressForm
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.


class ShippingAddressListView(ListView):
    template_name = "shipping_addresses/shipping_addresses.html"
    model = ShippingAddress

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by("-default")


def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()
        shipping_address.save()
        
        messages.success(request, "Dirección creada exitosamente")
        return redirect("shipping_addresses:shipping_addresses")

    return render(request, "shipping_addresses/create.html", {'form': form})
