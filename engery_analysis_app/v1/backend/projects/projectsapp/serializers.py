from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.Serializer):
    class Meta:
        model = Projects
        fields = ('__all__')


