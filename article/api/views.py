from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
)

from article.api.paginations import ArticlePagination
from article.api.permissions import IsOwner
from article.api.serializers import ArticleSerializer
from article.models import Article
from rest_framework.permissions import (
    IsAuthenticated,
)


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    pagination_class = ArticlePagination


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    # permission_classes = [IsOwner]
    #
    # def perform_update(self, serializer):
    #     serializer.save(author = self.request.user)


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]
    #
    # def perform_create(self, serializer):
    #     serializer.save(author = self.request.user)
