from django.urls import path
from . import views


urlpatterns = [
    path('', views.OthersPosts.as_view()),
    path('mypost', views.MyPosts.as_view()),
    path('mypost/<int:pk>', views.MyPosts.as_view()),
]
