from .models import Article, Category, Comment
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'category', 'title', 'publish_date', 'image_header', 'content', 'draft')
        extra_kwargs = {
            'draft': {'write_only': True}
        }
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )
        extra_kwargs = {
            'name': {'read_only': True}
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'comment_date_time', 'comment_user_id')
