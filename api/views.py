from rest_framework import mixins
from rest_framework import generics

from ig_private_api.api.models import Photo
from ig_private_api.api.serializers import PhotoSerializer


class PhotoList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Photo.objects.all().order_by('-created_at')
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PhotoDetail(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
