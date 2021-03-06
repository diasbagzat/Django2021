from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=255)
    create_date = serializers.DateField()
    dueon_date = serializers.DateField()
    owner = serializers.CharField(max_length=255)