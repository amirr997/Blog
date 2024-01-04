from django.db import models
from users.models import Profile
from .managers import PostManager


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    class Meta:
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f'{self.id} - {self.title}'


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name_plural = 'لایک ها'

    def __str__(self):
        return f'{self.id}'
