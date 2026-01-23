from django.conf import settings
from django.db import transaction
from django.template.defaultfilters import join
from rest_framework import serializers

from Users.models import PaisesChoices, CustomUser, Ciudades, InfoPersonal, Roles


class RegisterSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    apellidos = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    password1 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)
    password2 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)

    direccion = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    telefono = serializers.CharField(max_length=11)
    edad = serializers.IntegerField(required=True, min_value=0, max_value=100)
    ciudad = serializers.SlugField(required=True, allow_blank=False, allow_null=False, max_length=30)

    pais = serializers.ChoiceField(
        choices=PaisesChoices.choices,
        default=PaisesChoices.SPAIN,
        error_messages={"pais_Invalida": "El país elegido no es válido"}
    )

    class Meta:
        model = CustomUser
        fields = ('email',
                  'nombre',
                  'apellidos',
                  'password1',
                  'password2',
                  'direccion',
                  'telefono',
                  'edad',
                  'ciudad',
                  'pais')

    # validate => este método es la validación global para todo
    # validate_email, validate_nombre, validate_edad, ... -> validar de forma individual y personalizar la validacion
    def validate_email(self, email):
        if "@" not in email:
            raise serializers.ValidationError("El email es invalido.")
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise serializers.ValidationError(
                "El email tiene una de las extensiones no validas:" + ", " + join(settings.EXTENSIONES_BLACKLIST))
        return email

    def validate_password1(self, password1):
        if not any(n.isdigit() for n in password1):
            raise serializers.ValidationError("El password tiene que contener al menos un digito.")
        return password1

    def validate_telefono(self,telefono):
        try:
            int(telefono)
            return telefono
        except ValueError:
            raise serializers.ValidationError("El telefono no es valido.")

    def validate_ciudad(self,ciudad):
        check = Ciudades.objects.filter(slug=ciudad).exists()
        if not check:
            raise serializers.ValidationError("La ciudad no esta en nuestro registro.")
        return ciudad
    def validate_edad(self,edad):
        if edad < 18:
            raise serializers.ValidationError("Debes ser mayor de edad.")
        return edad
    def validate(self,attrs):# ATTRS es un dicionario que contiene todos los datos anteriores
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password1")

        ciudad = Ciudades.objects.filter(slug=validated_data["ciudad"]).first()
        role_por_defecto = Roles.objects.filter(default=True).first()
        if not role_por_defecto:
            raise serializers.ValidationError("Error desconocido no se pudo asignar el rol")



        personal_info = InfoPersonal.objects.create(
            direccion=validated_data["direccion"],
            telefono=validated_data["telefono"],
            edad=validated_data["edad"],
            ciudad=ciudad,
            pais=validated_data["pais"]
        )

        user= CustomUser.objects.create(
            email=validated_data["email"],
            nombre=validated_data["nombre"],
            apellidos=validated_data["apellidos"],
            personal_info=personal_info,
            role = role_por_defecto
        )

        user.set_password(password)
        user.save()

        return user
