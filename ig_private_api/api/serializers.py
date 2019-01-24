from rest_framework import serializers

from . import models


# The serializer responsible for turning an instance of the Photo class into a JSON string
# Extending HyperlinkedModelSerializer because it auto-generates a handy URL for us
class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Photo
        fields = ('id', 'description', 'image_path', 'created_at', 'modified_at', 'url')
