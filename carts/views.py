from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart(request):
    #Crear una sesion
    #request.session['cart_id'] = '123' # Diccionario
    #Obtenemos el valor de una sesion
    #v = request.session.get("cart_id")
    #print(v)
    # Eliminando una sesion
    #request.session['cart_id'] = None
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')

    if cart_id:
        # Obtenemos el carrito de la base de datos
        cart = Cart.objects.get(pk=request.session.get('cart_id'))
    else:
        # Creamos un nuevo carrito
        cart = Cart.objects.create(user=user)

    request.session['cart_id'] = cart.id

    return render(request, "carts/cart.html", {})