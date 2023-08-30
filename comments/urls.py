"""This module holds URL patterns for the paths in the comments apps."""

from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
]