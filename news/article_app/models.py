from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    link = models.URLField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=40)

    class Meta:
        ordering = ['upvotes']

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.TimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")




    

