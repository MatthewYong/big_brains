from django.urls import path
from . import views

urlpatterns = [
    path('<toy_id>', views.all_reviews, name='all_reviews'),
]
