#api 
from .serializers import ArticleSerializer, CategorySerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet, generics
#models
from . import models
# permissions, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from . import permissions, pagination
# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset = models.Article.objects.filter(draft=False)
    serializer_class = ArticleSerializer
    pagination_class = pagination.StandardResultsSetPagination
    permission_classes = [permissions.IsAdminUserOrReadOnly]

class CategoryViewSet(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class ArticleCategoryViewSet(generics.ListAPIView):
    queryset = models.Article.objects.filter(draft = False)
    serializer_class = ArticleSerializer
    pagination_class = pagination.StandardResultsSetPagination
    def get_queryset(self):
        cate = self.kwargs['category']
        return models.Article.objects.filter(draft = False, category = cate)

class CommentViewSet(generics.ListAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = pagination.CommentPagination
    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return models.Comment.objects.filter(comment_article_id = article_id)
