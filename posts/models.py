from django.db import models, transaction
from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f'{self.id} - {self.title}'
