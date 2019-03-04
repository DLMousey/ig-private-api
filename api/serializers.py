import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ('description', 'image_path', 'created_at', 'modified_at', 'owner')

    def create(self, data):
        return models.Photo.objects.create(**data)

    def update(self, instance, data):
        instance.description = data.get('description', instance.description)
        instance.image_path = data.get('image_path', instance.image_path)
        instance.modified_at = datetime.datetime.utcnow()

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'id')


class PhotoLikeSerializer(serializers.ModelSerializer):
    liked_by = UserSerializer(many=True, read_only=True)

    class Meta:
        model = models.PhotoLike
        fields = ('created_at', 'liked_by', 'photo')
