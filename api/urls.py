from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .data_views import photo_list, photo_detail, photo_like

urlpatterns = [
    path('photos/', photo_list.PhotoListView.as_view()),
    path('photos/<int:pk>', photo_detail.PhotoDetailView.as_view()),
    path('photos/<int:pk>/like', photo_like.PhotoLikeView.as_view()),
    url(r'^photos/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

urlpatterns = format_suffix_patterns(urlpatterns)
