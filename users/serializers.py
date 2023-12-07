from rest_framework import serializers
from .models import Profile, DirectMessages, ChatList


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatList
        fields = '__all__'


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessages
        fields = '__all__'
