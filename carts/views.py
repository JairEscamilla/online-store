from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart

# Create your views here.
def cart(request):
    #Crear una sesion
    #request.session['cart_id'] = '123' # Diccionario
    #Obtenemos el valor de una sesion
    #v = request.session.get("cart_id")
    #print(v)
    # Eliminando una sesion
    #request.session['cart_id'] = None
    cart = get_or_create_cart(request)

    return render(request, "carts/cart.html", {})