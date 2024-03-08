
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "StyleIT Admin"
admin.site.site_title = "Wellcome To StyleIT Portal"
admin.site.index_title = "Welcome to Supe Admin Panel!"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cart/', include('cart.urls'))
    
   
]
