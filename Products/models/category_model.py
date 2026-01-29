from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError


class Category(models.Model):
    nombre = models.CharField(max_length=50,unique=True,blank=False,null=False,verbose_name="Nombre",help_text="Nombre del categoria (Obligatorio)")
    slug = models.SlugField(unique=True,null=True,blank=True,verbose_name="Slug")
    creado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Categorías'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorías"

    def save(self,*args,**kwargs):
        if not self.slug:
            prov = slugify(self.nombre)
            cont = 0
            while Category.objects.filter(slug=prov).exists():
                prov = prov + "-"+str(cont)
                cont = cont + 1
            self.slug = prov
        categoria = Category.objects.filter(nombre=self.nombre).first()
        if categoria and categoria.id!=self.id:
            raise ValidationError({
                "nombre":["Ya existe un campo con este nombre"]
            })
        super().save(*args,**kwargs)



