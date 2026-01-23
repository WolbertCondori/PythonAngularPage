from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email or "@" not in email:
            raise ValueError('Usuario debe tener un correo valido')
        if not password:
            raise ValueError('Contraseña no valida')
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise ValueError(f'No te voy a dejar crear una cuenta. Formatos no permitidos: '+', '.join(settings.EXTENSIONES_BLACKLIST))
        email=self.normalize_email(email)
        extra_fields['email']=email

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not password:
            raise ValueError('Contraseña no valida')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
     email = models.EmailField(max_length=100, unique=True,blank=False,null=False)
     nombre = models.CharField(max_length=30, blank=False,null=False)
     apellidos = models.CharField(max_length=50, blank=False,null=False)
     is_active = models.BooleanField(default=True,verbose_name='¿Está Activo?')

     role = models.ForeignKey('Roles',on_delete=models.SET_NULL,null=True,blank=True)
     personal_info=models.ForeignKey('InfoPersonal',on_delete=models.CASCADE,null=True,blank=True)


     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)
     objects = CustomUserManager()
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []

     class Meta:
         db_table = 'users'
         ordering = ('is_superuser','is_active','email')
         verbose_name = 'Usuario'
         verbose_name_plural = 'Usuarios'