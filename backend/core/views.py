# core/views.py

from rest_framework import viewsets
from .models import Blueprint, Project
from .serializers import BlueprintSerializer, ProjectSerializer

class BlueprintViewSet(viewsets.ModelViewSet):
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
