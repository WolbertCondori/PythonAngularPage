from django.conf import settings
from django.template.defaultfilters import join
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import CustomUser


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False,allow_blank=True,allow_null=True,max_length=100)
    telefono = serializers.CharField(required=False,max_length=11,allow_blank=True,allow_null=True)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)

    class Meta:
        model = CustomUser
        fields = ('email', 'telefono', 'password')

    def validate_email(self, email):
        if email:
            if "@" not in email:
                raise serializers.ValidationError("El email es invalido.")
            if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
                raise serializers.ValidationError(
                    "El email tiene una de las extensiones no validas:" + ", " + join(settings.EXTENSIONES_BLACKLIST))
            if not CustomUser.objects.filter(email=email).exists():
                raise serializers.ValidationError("El correo que ingreso no tiene una cuenta vinculada")
        return email

    def validate_telefono(self, telefono):
        if telefono:
            try:
                int(telefono)
                if not CustomUser.objects.filter(personal_info__telefono=telefono).exists():
                    raise serializers.ValidationError("El numero de teléfono introduction no esta registrado")
            except ValueError:
                raise serializers.ValidationError("El numero de telefono introducido no es valido")
        return telefono
    def validate_password(self, password):
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("El password tiene que contener al menos un digito.")
        return password

    def validate(self, attrs):
        user = None
        if  attrs.get("email"):
            user = CustomUser.objects.filter(email=attrs['email']).first()
        elif attrs.get('telefono'):
            user = CustomUser.objects.filter(personal_info__telefono=attrs['telefono']).first()
        if not user.check_password(attrs['password']) and user:
            raise serializers.ValidationError({"password":"Contraseña incorrecta"})

        refresh = RefreshToken.for_user(user)
        refresh["nombre"]=user.nombre
        refresh["pais"]=user.personal_info.pais


        return {
            "success":True,
            "data":{
                "nombre":user.nombre,
                "email":user.email,
                "rol":user.role.nombre,
                "telefono":user.personal_info.telefono if user.personal_info.telefono else "",
                "refresh_token":str(refresh),
                "token":str(refresh.access_token)
            }
        }


