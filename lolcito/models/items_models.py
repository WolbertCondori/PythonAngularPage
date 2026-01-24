from django.db import models
from django.utils.text import slugify


class DamageTypes(models.TextChoices):
    ATTACK_DAMAGE = "AD","Attack Damage"
    POWER_HABILITY = "PH","Power Hability"
    TRUE_DAMAGE = "TD","True Damage"


class Items(models.Model):
    nombre = models.CharField(editable=True,max_length=25,unique=False,blank=False,null=False,verbose_name="Nombre")
    price = models.CharField(max_length=4,unique=False,blank=False,null=False,verbose_name="Price")
    description = models.CharField(max_length=250,unique=True,blank=False,null=False,verbose_name="Description")
    damageType = models.CharField(choices=DamageTypes.choices,default=DamageTypes.ATTACK_DAMAGE,max_length=4,blank=False,null=False,verbose_name="Damage Type")

    class Meta:
        db_table = 'Items'
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


