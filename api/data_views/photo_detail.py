from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Photo
from ..serializers import PhotoSerializer


class PhotoDetailView(APIView):
    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        serializer = PhotoSerializer(self.get_object(pk))
        return Response(serializer.data)
