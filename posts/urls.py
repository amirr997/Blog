from django.urls import path
from . import views


urlpatterns = [
    path('', views.OthersPosts.as_view(), name='others-posts'),
    path('mypost', views.MyPosts.as_view()),
    path('mypost/<int:pk>', views.MyPosts.as_view()),

    path('search', views.Search.as_view()),
]
