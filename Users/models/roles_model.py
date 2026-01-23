import secrets

from django.db import models


# roles_djangoadmindsfhlksdnghlksdnfhklsd
class Roles(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True,verbose_name='¿Está Activo?')
    default = models.BooleanField(default=False,verbose_name="¿Rol por Defecto?")


    class Meta:
        db_table = 'roles'
        ordering = ['nombre']
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    # este método es llamado al guardar o actualizar
    def save(self, *args, **kwargs):
        if not self.slug:
            # Entonces creamos slug unico
            prov = secrets.token_hex(16)
            while Roles.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov

        role_con_default = Roles.objects.filter(default=True).first()

        if role_con_default and self.default and role_con_default.id != self.id:
            self.default = False


        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

