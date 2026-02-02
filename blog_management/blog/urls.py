from django.urls import path
from blog.views import (
    BlogListView, BlogDetailView, CommentListView, CommentDetailView
    )


urlpatterns = [
    path("blogs/", BlogListView.as_view()),
    path("blogs/<int:pk>", BlogDetailView.as_view()),
    path("comments/", CommentListView.as_view()),
    path("comments/<int:pk>", CommentDetailView.as_view())
]