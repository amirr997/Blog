from rest_framework import serializers
from .models import Comment
from users.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

