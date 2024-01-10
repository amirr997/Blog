from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
# from .tasks import test_task1
from django.db.models import Q
from django.db.models import Count, Avg


class Search(APIView):
    def get(self, request):
        text = request.GET.get('text')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        posts = Post.objects.filter((Q(text__icontains=text) | Q(title__icontains=text)) & Q(created_at__gte=from_date))
        data = PostSerializer(posts, many=True).data
        return Response(data)


class OthersPosts(APIView):

    def get(self, request):
        posts = Post.objects.all().only('title','text')
        posts = Post.objects.annotate(likes_count=Count('likes')).filter(likes_count__gte=1)
        views_average = Post.objects.aggregate(views_avg=Avg('views'))
        data = PostSerializer(posts, many=True).data
        return Response(data)


class MyPosts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(user=request.user.profile)
        data = PostSerializer(posts, many=True).data
        return Response(data)

    def post(self, request):
        post = Post.objects.create(title=request.data['title'],
                                   user=request.user.profile,
                                   text=request.data['text'])
        data = PostSerializer(post).data
        return Response(data)

    def put(self, request):
        post = Post.objects.get(id=request.data['id'], user=request.user.profile)
        post.title = request.data['title']
        post.text = request.data['text']
        post.save()
        data = PostSerializer(post).data
        return Response(data)

    def delete(self, request, pk):
        Post.objects.get(id=pk, user=request.user.profile).delete()
        return Response({'msg': 'deleted'})


# class TestCelery(APIView):
#     def post(self, request):
#         be_done_at = request.data['be_done_at']
#         test_task1.apply_async(eta=be_done_at)
#         return Response({'msg': 'ok'})
