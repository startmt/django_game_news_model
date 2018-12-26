from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('news', views.ArticleViewSet)
urlpatterns = [    
    path('', include(router.urls)),
    path('news/<int:article_id>/comments', views.CommentViewSet.as_view()),
    path('category/', views.CategoryViewSet.as_view()),
    path('category/<int:category>/', views.ArticleCategoryViewSet.as_view()),
    path('user/', include('rest_registration.api.urls')),
]
