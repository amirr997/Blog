from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    personal_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.personal_id}'


class ChatList(models.Model):
    user_one = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user1_chats')
    user_two = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user2_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'چت ها'

    def __str__(self):
        return f'{self.id}'


class DirectMessages(models.Model):
    chat = models.ForeignKey(ChatList, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return f'{self.id}'
