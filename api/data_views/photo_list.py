from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Photo
from ..serializers import PhotoSerializer


class PhotoListView(APIView):
    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)