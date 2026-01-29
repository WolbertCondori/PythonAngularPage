from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError


class Products(models.Model):
    nombre = models.CharField(max_length=100,null=False,blank=False,unique=True,verbose_name="Nombre")
    precio = models.DecimalField(max_digits=5, decimal_places=2,null=False,blank=False,verbose_name="Precio")
    categoria = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Categoria")
    descripcion = models.TextField(verbose_name="Descripcion",max_length=500)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True,verbose_name="Slug")
    is_active = models.BooleanField(default=True,verbose_name="¿Esta Activo?")
    creado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")

    class Meta:
        db_table = "Productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-categoria__nombre','-nombre']

    def __str__(self):
        return f"[Producto: {self.nombre}-{self.precio}-{self.categoria.nombre}]"

    def save(self,*args,**kwargs):
        if not self.slug:
            prov = slugify(self.nombre)
            cont = 0
            while Products.objects.filter(slug=prov).exists():
                prov = prov + "-"+str(cont)
                cont = cont + 1
            self.slug = prov
        nombre = Products.objects.filter(nombre=self.nombre).first()
        if nombre and nombre.id != self.id:
            raise ValidationError({
                "nombre": ["Ya existe un campo con este nombre"]
            })
        super().save(*args,**kwargs)
