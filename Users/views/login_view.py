from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.serializers import LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    # Methods GET/POST/PUT/PATCH/DELETE
    def post(self, request):
        # request = nombre, apellido, edad, ciudad, pais,
        # dirección, contraseña, repetir contraseña, teléfono .
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)