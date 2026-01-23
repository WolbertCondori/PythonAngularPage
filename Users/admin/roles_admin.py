from django.contrib import admin

from Users.models import Roles

class RolesAdmin(admin.ModelAdmin):
    list_display = ('nombre','is_active','slug','default')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    list_editable = ('is_active','default')
    readonly_fields = ('slug',)
    fieldsets = (
    ("Información",{'fields':('nombre',)}),
    ("configuración",{'fields':('is_active','default','slug')}),
    )
    list_per_page = 15

admin.site.register(Roles, RolesAdmin)