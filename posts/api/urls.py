from django.urls import path,include
from . import views

from .views import (PostListView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                    PostLikeCreateView,
                    PostLikeListView,
                    PostCreateView)
urlpatterns = [
    path('',PostListView.as_view(),name='post_list_api'),  
    path('add_post/',PostCreateView.as_view(),name='add_post_api'), 
    path('<int:pk>/like/',PostLikeCreateView.as_view(),name='like_post_api'),
    path('<int:pk>/likes/',PostLikeListView.as_view(),name='post_likes_api'),
    path('<int:pk>/',PostDetailView.as_view(),name='post_detail_api'),
    path('<int:pk>/comments/',include('comments.api.urls')),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='post_update_api'), 
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete_api'), 
]