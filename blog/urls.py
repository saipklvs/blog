from django.conf.urls import url
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView
    )

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^about/', views.about, name='blog-about'),
] 