from django.shortcuts import render ,get_object_or_404
from .cart import Cart
from  home.models import ShopIT
from django.http  import JsonResponse

def cart_summary(request):
    return  render(request, 'cart/cart_summary.html',{})

def cart_add(request):
    cart =  Cart(request)
    if request.POST.get('action')=='post':
        ShopIT_id=int(request.POST('ShopIT_Id'))

        shopIT = get_object_or_404(ShopIT, id=ShopIT_id)
        cart.add(ShopIT=shopIT)
        response =JsonResponse({'Product Name:': ShopIT.name })
        return response
    
    

def cart_delete(request):
    pass

def cart_update(request):
    pass