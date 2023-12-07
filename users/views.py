from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, DirectMessages, ChatList
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .serializers import DirectMessageSerializer, ChatListSerializer


class UserRegister(APIView):
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        personal_id = request.data['personal_id']
        password = request.data['password']

        user = User.objects.create_user(username=personal_id,
                                        password=password,
                                        is_staff=False,
                                        is_superuser=False,)

        Profile.objects.get_or_create(user=user,
                                      first_name=first_name,
                                      last_name=last_name,
                                      personal_id=personal_id,)

        refresh = RefreshToken.for_user(user)
        final_object = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return Response(final_object)


class DirectMessageView(APIView):
    def post(self, request):
        sender = request.user.profile
        chat = ChatList.objects.get(id=request.data['chat_id'])
        message = request.data['message']
        DirectMessages.objects.create(sender=sender, chat=chat, message=message)
        return Response('sent message')

    def get(self, request, pk):
        user = request.user.profile
        chat = ChatList.objects.get(Q(user_one=user) | Q(user_two=user), id=pk)
        messages = DirectMessages.objects.filter(chat=chat)
        data = DirectMessageSerializer(messages, many=True).data
        return Response(data)


class ChatListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_one = request.user.profile
        user_two = Profile.objects.get(id=request.data['user_id'])
        ChatList.objects.create(user_one=user_one, user_two=user_two)
        return Response('start chat')

    def get(self, request):
        user = request.user.profile
        directs = ChatList.objects.filter(Q(user_one=user) | Q(user_two=user))
        data = ChatListSerializer(directs, many=True).data
        return Response(data)
