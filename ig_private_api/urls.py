from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from .api import views

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
