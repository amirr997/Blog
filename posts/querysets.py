from django.db import models


class PostQuerySet(models.QuerySet):
    def actives(self, *args, **kwargs):
        return super(PostQuerySet, self).filter(*args, **kwargs).filter(is_active=True)
