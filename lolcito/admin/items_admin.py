from django.contrib import admin

from lolcito.models import Items


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('nombre','price','description','damageType')
    list_filter = ('price','nombre',)
    search_fields = ('nombre',)
    list_editable = ('price','description',)
    fieldsets = (
    ("Información",{'fields':('nombre','price','description',)}),
    ("configuración",{'fields':('damageType',)}),
    )
    add_fieldsets = (
    ("Información",{'fields':('nombre','price','description',)}),
    )
    list_per_page = 15

admin.site.register(Items, ItemsAdmin)