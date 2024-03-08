from django.shortcuts import render , HttpResponse
from .models import ShopIT

# Create your views here.
def index(request):
    shopIT = ShopIT.objects.all() 
    return render(request,"index.html",{'shopIT':shopIT})
    # return HttpResponse(" My self Piyush yadav")
def about(request):
    #return HttpResponse("zoro is lost again!!! ")
    return render ( request, 'about.html')

def add(request):
    return render ( request, 'add.html')

def contact(request):
    return render ( request, 'contact.html')
def base(request):
    return render ( request, 'base.html')

def recently(request):
    shopIT = ShopIT.objects.all()  
    return render ( request, 'recently.html', {'shopIT':shopIT})

def admin(request):
    return HttpResponse('admin/.urls')
