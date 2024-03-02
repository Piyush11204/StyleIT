from django.shortcuts import render , HttpResponse
from .models import ShopIT

# Create your views here.
def index(request):

    return render(request,"index.html")
    # return HttpResponse(" My self Piyush yadav")
def about(request):
    #return HttpResponse(" I am for vidyaverdini's college of engineering and technology")
    return render ( request, 'about.html')

def add(request):
    return render ( request, 'add.html')

def contact(request):
    return render ( request, 'contact.html')
def base(request):
    return render ( request, 'base.html')

def recently(request):
    shopIT = ShopIT.objects.all()  # get the last 5 records
    return render ( request, 'recently.html', {'shopIT':shopIT})

def admin(request):
    return HttpResponse('admin/.urls')
