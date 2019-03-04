from datetime import datetime

from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import PhotoLike, Photo
from ..serializers import PhotoLikeSerializer


class PhotoLikeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_photo(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExit:
            raise Http404

    '''
        Create a 'like' from the currently logged in user for a given
        photo, if the user has already 'liked' the photo, the record will be removed
    '''
    def post(self, request, pk):
        try:
            photoLikes = PhotoLike.objects.get(user__pk=request.user.pk, photo__pk=pk)
        except PhotoLike.DoesNotExist:
            like = PhotoLike()
            like.created_at = datetime.utcnow()
            like.user = request.user
            like.photo = self.get_photo(pk)
            PhotoLike.save(like)

            serializer = PhotoLikeSerializer(like, many=False)
            return Response(serializer.data, 201)

        PhotoLike.delete(photoLikes)
        return Response({}, 204)