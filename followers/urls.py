"""This module holds URL patterns for the paths in the likes apps."""

from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>', views.FollowerDetail.as_view()),
]
