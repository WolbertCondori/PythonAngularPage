from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Tienda de Camilo"
admin.site.site_title = "Administración"
admin.site.index_title = "Administración 1.0.0"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Users.urls')),
]
