from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import PhotoLike
from .serializers import PhotoLikeSerializer


class Like(mixins.CreateModelMixin,
           mixins.DestroyModelMixin,
           generics.GenericAPIView):
    queryset = PhotoLike.objects.all()
    serializer_class = PhotoLikeSerializer

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
