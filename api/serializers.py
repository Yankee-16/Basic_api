from api.models import student
from rest_framework import serializers


class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return student.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.gat('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
