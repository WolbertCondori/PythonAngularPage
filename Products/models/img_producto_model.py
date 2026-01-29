from django.db import models


class Imagen(models.Model):
    producto = models.OneToOneField("Products",on_delete=models.CASCADE,related_name="imagen")
    image = models.ImageField(upload_to="images/",blank=False,null=False)
    creado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")

    def __str__(self):
        return f"[IMAGEN DEL PRODUCTO: {self.producto.nombre}]"


    class Meta:
        db_table = "Imagenes"
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = ['producto__nombre']

    def save(self,*args,**kwargs):
        if self.image:
            nombre_imagen = self.producto.slug
            extencion = self.image.name.split(".")[-1]
            self.image.name = f"{nombre_imagen}.{extencion}"
        super().save(*args,**kwargs)
