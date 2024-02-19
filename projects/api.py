from .models import Project
from rest_framework import viewsets, permissions

from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()# hace la consulta a la base de datos todos los objetos
    permission_classes=[permissions.AllowAny]# permite cualquiera a ver la api
    serializer_class=ProjectSerializer# selecciona el serializer que se va a utilizar