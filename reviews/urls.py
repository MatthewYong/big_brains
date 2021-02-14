from django.urls import path
from . import views

urlpatterns = [
    path('<int:toy_id>/', views.view_toy_review, name='view_toy_review'),
    path('review/<int:toy_id>', views.add_toy_review, name='add_toy_review'),
]
