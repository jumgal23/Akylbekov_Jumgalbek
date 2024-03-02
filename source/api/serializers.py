from rest_framework import serializers

from webapp.models import Todolist


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=150)
    completed = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)

