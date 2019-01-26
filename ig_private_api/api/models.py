from django.db import models


class Photo(models.Model):
    description = models.TextField()
    image_path = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
