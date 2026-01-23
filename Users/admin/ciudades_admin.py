from django.contrib import admin
from Users.models import Ciudades

@admin.register(Ciudades)
class CiudadesAdmin(admin.ModelAdmin):
    list_display = ("nombre","slug")
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    readonly_fields = ('slug',)
    list_per_page = 5