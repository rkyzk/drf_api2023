"""This module holds URL patterns for the paths in the likes apps."""

from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>', views.LikeDetail.as_view()),
]
