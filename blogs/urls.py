from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('<blog_id>', views.blog_detail, name='blog_detail'),
    path('blogs/blog_add/', views.blog_add, name='blog_add'),
    path('blogs/<blog_id>', views.blog_delete, name='blog_delete'),
]
