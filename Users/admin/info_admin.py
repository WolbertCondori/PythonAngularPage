from django.contrib import admin
from Users.models import InfoPersonal


class InfoAdmin(admin.ModelAdmin):
    list_display = ('telefono','direccion','ciudad','pais','edad')
    search_fields = ("telefono",)
    list_filter = ("ciudad","pais")
    list_per_page = 25
admin.site.register(InfoPersonal,InfoAdmin)