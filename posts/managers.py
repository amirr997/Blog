from django.db import models
from .querysets import PostQuerySet


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def actives(self, *args, **kwargs):
        return self.get_queryset().actives(*args, **kwargs)
