from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .data_views import photo_list, photo_detail, photo_like

urlpatterns = [
    path('photos/', photo_list.PhotoListView.as_view()),
    path('photos/<int:pk>', photo_detail.PhotoDetailView.as_view()),
    path('photos/<int:pk>/like', photo_like.PhotoLikeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
