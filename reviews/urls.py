from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:toy_id>', views.add_toy_review, name='add_toy_review'),
]
