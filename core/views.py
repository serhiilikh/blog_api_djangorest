from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Upvote, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        upvote = Upvote.objects.get_or_create(post=post)
        return Response(upvote)
