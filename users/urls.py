from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    path('chat/list/', views.ChatListView.as_view()),

    path('chat/message/', views.DirectMessageView.as_view()),
    path('chat/message/<int:pk>/', views.DirectMessageView.as_view()),
]
