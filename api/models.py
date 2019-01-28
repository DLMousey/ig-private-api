from django.db import models


class Photo(models.Model):
    description = models.TextField()
    image_path = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
