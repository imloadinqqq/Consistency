from django.urls import path, include
from django.db import models
from rest_framework import routers, serializers, viewsets

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Consistency.settings')  # Replace 'Consistency' with your project name
django.setup()

# Task Model
class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_desc = models.CharField(max_length=250)
    task_freq = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'task', 'desc', 'freq', 'created']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.bjects.all()
    serializer_class = TaskSerializer
    
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]