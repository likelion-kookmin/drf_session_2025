from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView, ArticleViewSet, ArticleGenericViewSet

urlpatterns = [
    path('apiview/', ArticleListCreateView.as_view()),
    path('apiview/<int:pk>/', ArticleDetailView.as_view()),
    path('viewset/', ArticleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('viewset/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]



    # path('genericviewset/', ArticleGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('genericviewset/<int:pk>/', ArticleGenericViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),