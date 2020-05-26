from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from article_app.models import Article, Comment
from article_app.serializers import ArticleSerializer, ArticleUpdateSerializer, CommentSerializer, CommentUpdateSerializer


class BaseView(APIView):

    def get_object(self, model, id):
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise Http404


class ArticleListView(BaseView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleView(APIView):
    
    def get(self, request):
        article = self.get_object(Article, article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, article_id):
        article = self.get_object(Article, article_id)
        serializer = ArticleUpdateSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, article_id):
        article = self.get_object(Article, article_id)
        article.upvotes += 1
        article.save()
        
    def delete(self, request, article_id):
        article = self.get_object(Article, article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListView(BaseView):

    def get(self, request, article_id, format=None):
        article = self.get_object(Article, article_id)
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, article_id, format=None):
        data = request.data
        data['article'] = article_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):

    def put(self, request, article_id, comment_id, format=None):
        comment = Comment.objects.get(id=comment_id)

        serializer = CommentUpdateSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, comment_id, format=None):
        comment = self.get_object(Comment, comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

