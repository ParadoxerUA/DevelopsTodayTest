from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from article_app.models import Article
from article_app.serializers import ArticleSerializer


class ArticleView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, format=None)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):

    def get(self, request, pk, format=None):
        pass

    def post(self, request, pk, format=None):
        pass

    def patch(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass