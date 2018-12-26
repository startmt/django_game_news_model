from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    image_header = models.ImageField(upload_to="images", blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    comment_article_id = models.ForeignKey(Article, related_name='comment', on_delete = models.CASCADE)
    comment_date_time = models.DateTimeField(auto_now=True)
    comment = models.TextField()
