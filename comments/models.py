from django.db import models
from users.models import Profile
from posts.models import Post


class Comment(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.text[:30]}'
