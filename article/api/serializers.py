from rest_framework import serializers
from article.models import Article


class ArticleSerializer (serializers.ModelSerializer):
    author = serializers.CharField (max_length = 120)

    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'title',
            'content',
            'liked',
        ]
