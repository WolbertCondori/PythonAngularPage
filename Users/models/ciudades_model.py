from django.db import models
from django.utils.text import slugify


class Ciudades(models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False,verbose_name="Nombre de Ciudad")
    slug = models.SlugField(max_length=30,null=False,blank=False,verbose_name="Slug")


    class Meta:
        db_table = 'ciudades'
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre