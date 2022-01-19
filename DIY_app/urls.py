from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('posts/', views.PostList.as_view(), name = 'post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name = 'post_list'),
]