from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
  
   path("", views.index, name='home'),
   path("home",views.index, name= 'home'), 
   path("about", views.about, name='about'),
   path("add", views.add, name='add'),
   path("contact", views.contact, name='contact'),
   path("recently", views.recently, name='recently'),
   path("admin/", views.admin, name='admin'),
   ]