from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import CustomUser, InfoPersonal


class InfoPersonalInline(admin.StackedInline):
    model = InfoPersonal
    can_delete = False
    verbose_name = "Informacion Personal"
    verbose_name_plural = "Datos Personales"
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (InfoPersonalInline,)
    model = CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','nombre','is_active','is_superuser','last_login','role__nombre','personal_info') # Esto es las columnas en mi panel de administración
    list_filter = ('is_active','is_superuser')
    search_fields = ('email','nombre')
    # añadir un campo editable
    list_editable = ('is_active',)
    # añade páginas con un límite de campos a mostrar
    list_per_page = 5

    fieldsets = (
    ("Informacion",{'fields':('nombre','email')}),
    ("Configuracion", {'fields': ('password','role','is_active')})
    )

    add_fieldsets = (
    ("Informacion Personal",{'fields':('nombre','apellidos','personal_info'),
                    'classes':('wide',)}),
    ("Informacion de iniciar sesion",
     {'classes':('wide',),
      'fields':('email','password1','password2')}
     ),
    )

admin.site.register(CustomUser, UserAdmin)




