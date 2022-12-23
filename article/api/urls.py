from django.urls import path
from .views import (
    ArticleListAPIView,
    ArticleDetailAPIView,
    ArticleDeleteAPIView,
    ArticleUpdateAPIView,
    ArticleCreateAPIView,
)


urlpatterns = [
    path('list',ArticleListAPIView.as_view(),name='list'),
    path('detail/<pk>', ArticleDetailAPIView.as_view(), name='detail'),
    path('delete/<pk>', ArticleDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', ArticleUpdateAPIView.as_view(), name='update'),
    path('create', ArticleCreateAPIView.as_view(), name='create'),

]
