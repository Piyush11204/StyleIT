from django.contrib import admin
from .models import ShopIT


class  ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quantity')

admin.site.register(ShopIT, ShopAdmin)
