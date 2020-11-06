from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    link = models.CharField(max_length=1000, blank=False)
    author = models.CharField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=1000, blank=False)
