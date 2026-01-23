from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    # Methods GET/POST/PUT/PATCH/DELETE
    def post(self, request):
        # request = nombre, apellido, edad, ciudad, pais,
        # dirección, contraseña, repetir contraseña, teléfono .
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success':True},status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

