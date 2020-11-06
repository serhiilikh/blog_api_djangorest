from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import Post, Upvote, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class UpvoteSerializer(ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    upvote_count = SerializerMethodField("get_upvote_count")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "upvote_count",
            "author",
            "created",
        )

    @staticmethod
    def get_upvote_count(post):
        return Upvote.objects.filter(post=post).count()
