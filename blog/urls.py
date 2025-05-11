from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    
    path('authors/', views.AuthorListCreateView.as_view()),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view()),
]
