from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        comment = Comment.objects.create(user_profile=request.user.profile,
                                         post_id=request.data['post_id'],
                                         text=request.data['comment'])
        data = CommentSerializer(comment).data
        return Response(data)

    def get(self, request):
        comments = Comment.objects.filter(user_profile=request.user.profile)
        data = CommentSerializer(comments, many=True).data
        return Response(data)

    def put(self, request):
        comment = Comment.objects.get(id=request.data['id'])
        comment.text = request.data['comment']
        comment.save()
        data = CommentSerializer(comment).data
        return Response(data)

    def delete(self, request, pk):
        Comment.objects.get(id=pk).delete()
        return Response({'msg': 'deleted'})

