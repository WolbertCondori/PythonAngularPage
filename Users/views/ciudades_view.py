from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import Ciudades


class CiudadesView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        ciudades = Ciudades.objects.all().order_by('nombre')
        data = [{
            'nombre':ciudad.nombre,
            'slug': ciudad.slug
        }
            for ciudad in ciudades]
        return Response({"data":data,"success":True}, status=status.HTTP_200_OK)