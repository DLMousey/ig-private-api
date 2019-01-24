from django.db import models


class Photo(models.Model):
    id = models.UUIDField()
    description = models.TextField()
    image_path = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()


class Tag(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_length=16)
    photo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING, related_name='tags')
