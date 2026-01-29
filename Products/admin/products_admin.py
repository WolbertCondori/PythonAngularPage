from django.contrib import admin

from Products.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','descripcion','categoria__nombre','slug','is_active','creado','actualizado')
    list_filter = ('precio','categoria__nombre',)
    search_fields = ('nombre','precio','categoria__nombre')
    list_editable = ('precio','descripcion','is_active',)
    fieldsets = (
    ("Información",{'fields':('nombre','precio','descripcion',)}),
    ("configuración",{'fields':('is_active','categoria')}),
    )
    add_fieldsets = (
    ("Información",{'fields':('nombre','price','description',)}),
    )
    list_per_page = 15

admin.site.register(Products, ProductsAdmin)