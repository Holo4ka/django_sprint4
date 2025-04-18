"""Настройки адресов приложения blog"""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post, name='create_post'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('posts/<int:post_id>/comment/', views.comment, name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit_profile/', views.edit_profile,
         name='edit_profile')
]
