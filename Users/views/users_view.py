from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import CustomUser


class UsersView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        users = CustomUser.objects.all()
        data=[{
                'nombre':user.nombre,
                'apellidos':user.apellidos,
                'email':user.email,
                'is_active':user.is_active,
                'is_staff':user.is_staff,
                'is_superuser':user.is_superuser,
            }
            for user in users]
        return Response({'data':data},status=status.HTTP_200_OK)

