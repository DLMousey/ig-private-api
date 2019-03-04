from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class SystemUser(AbstractUser):
    def __str__(self):
        return self.username


class Photo(models.Model):
    description = models.TextField()
    image_path = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    owner = models.ForeignKey(SystemUser, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


class PhotoLike(models.Model):
    created_at = models.DateTimeField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        super(PhotoLike, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(PhotoLike, self).delete(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


class UserFollow(models.Model):
    user = models.ForeignKey(SystemUser, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(SystemUser, related_name='follower', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(UserFollow, self).save(*args, **kwargs)
