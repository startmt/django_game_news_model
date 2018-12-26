from django.contrib import admin
from .models import Category, Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header',               {'fields': ['category', 'title', 'publish_date', 'image_header']}),
        ('Body', {'fields': ['content']}),
        ('Draft', {'fields': ['draft']}),
    ]
    list_display = ('title', 'publish_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_user_id', 'comment_article_id', 'comment_date_time')

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)