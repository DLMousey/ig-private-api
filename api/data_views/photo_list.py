from datetime import datetime
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

from ..models import Photo
from ..serializers import PhotoSerializer


class PhotoListView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser)

    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request):
        if 'file' not in request.data:
            return Response({'error': 'No file found in request'}, 400)

        if 'description' not in request.data:
            return Response({'error': 'A description is required'}, 400)

        photo = Photo()
        photo.description = request.data['description']
        photo.image_path = request.data['file']
        photo.created_at = datetime.utcnow()
        photo.modified_at = datetime.utcnow()
        photo.owner = request.user

        Photo.save(photo)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, 201)
