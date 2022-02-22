from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_blog_post/<slug:slug>/',
         views.edit_blog_post, name='edit_blog_post'),
    path('delete_blog_post/<slug:slug>/',
         views.delete_blog_post, name='delete_blog_post'),
    path('<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
]
