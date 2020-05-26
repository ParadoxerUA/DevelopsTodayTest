from rest_framework import serializers
from article_app.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'link', 'creation_date', 'upvotes', 'author_name', 'comments']


class ArticleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'link']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date', 'article']


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content']

