from django.db import models


class Photo(models.Model):
    description = models.TextField()
    image_path = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    # todo - re-enable once auth system is in place
    # owner = models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
