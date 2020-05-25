from django.db import models
from django.template.defaultfilters import slugify


class Comment(models.Model):
    author_name = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.TimeField(auto_now_add=True)
    #replyes = models.ForeignKey()

class Article(models.Model):
    title = models.CharField(max_length=60)
    link = models.SlugField(max_length=60, unique=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=40)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        ordering = ['upvotes']

    def save(self, *args, **kwargs):
        self.link = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

