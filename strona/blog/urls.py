from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView ,PostUpdateView, PostDeleteView, UserPostListView, TagListView ,FindListView
from . import views


urlpatterns = [
    path('', PostListView.as_view() ,name='home'),
    path('user/<str:username>', UserPostListView.as_view() ,name='user-posts'),
    path('post/<slug:slug>', TagListView.as_view() ,name='tagged'),
    path('post/<int:pk>/', PostDetailView.as_view() ,name='post-detail'),
    path('post/new/', PostCreateView.as_view() ,name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() ,name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() ,name='post-delete'),
    path('post/find/', FindListView.as_view() ,name='find'),
    path('about/', views.about,name='about'),
]
