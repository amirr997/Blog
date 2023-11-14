from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


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
