from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Liste des tâches et création d'une nouvelle tâche
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Détail, mise à jour et suppression d'une tâche
class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
