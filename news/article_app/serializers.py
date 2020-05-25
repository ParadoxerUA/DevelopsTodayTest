from rest_framework import serializers

from article_app.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    link = serializers.HiddenField(default='')
    upvotes = serializers.HiddenField(default=0)
    
    class Meta:
        model = Article
        fields = '__all__'
        