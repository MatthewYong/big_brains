from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:toy_id>', views.add_toy_review, name='add_toy_review'),
    path('delete_toy_review/<int:review_id>/',
         views.delete_toy_review, name='delete_toy_review'),
]
