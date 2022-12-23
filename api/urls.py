from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView,
)
app_name = "post"

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<pk>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', PostUpdateAPIView.as_view(), name='update'),
    path('create', PostCreateAPIView.as_view(), name='create'),

]
