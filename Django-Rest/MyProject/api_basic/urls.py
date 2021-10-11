from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import ArticleAPIView, ArticleDetails, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    #path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]
