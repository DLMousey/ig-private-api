from rest_framework import serializers
import datetime

from . import models


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=True, allow_blank=True)
    image_path = serializers.CharField(required=True)
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

    def create(self, data):
        return models.Photo.objects.create(**data)

    def update(self, instance, data):
        instance.description = data.get('description', instance.description)
        instance.image_path = data.get('image_path', instance.image_path)
        instance.modified_at = datetime.datetime.utcnow()

        instance.save()
        return instance
