from rest_framework import serializers
from .models import Post, Comment
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class CommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id text post rating'.split()

class PostListSerializer(serializers.ModelSerializer):
    comments = CommentItemSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    comments1 = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = "title text created_date comments comments1 comments_count".split()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_comments1(self, post):
        comments =Comment.objects.filter(rating__gt=3, post=post)
        data = CommentItemSerializer(comments, many=True).data
        return data