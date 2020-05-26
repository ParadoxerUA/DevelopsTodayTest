from django.urls import path

from .views import ArticleView, ArticleListView, CommentView, CommentListView


app_name = "articles"

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:article_id>/', ArticleView.as_view()),
    path('articles/<int:article_id>/comments/', CommentListView.as_view()),
    path('articles/<int:article_id>/comments/<int:comment_id>/', CommentView.as_view())
]