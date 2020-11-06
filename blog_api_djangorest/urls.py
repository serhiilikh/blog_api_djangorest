from django.urls import include, path

from rest_framework import routers

from core.views import CommentViewSet, PostViewSet, UpvoteView


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/posts/upvote/post=<int:pk>/", UpvoteView.as_view()),
]
