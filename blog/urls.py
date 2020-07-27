from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('en/', blog_views.blog_en, name='blog-en'),
    
    path('categories/<str:cat>', blog_views.category, name='cat'),
    path('en/categories/<str:cat>', blog_views.category_en, name='cat-en'),
    
    path('search', blog_views.blog_search, name='blog-search'),
    path('en/search', blog_views.blog_search_en, name='blog-search-en'),

    path('<int:post_id>/', blog_views.post , name='post'),
    path('en/<int:post_id>/', blog_views.post_en , name='post-en'),
]