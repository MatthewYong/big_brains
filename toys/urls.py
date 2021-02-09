from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_toys, name='toys'),
    path('<toy_id>', views.toy_detail, name='toy_detail'),
    path('', views.all_reviews, name='all_reviews'),
]
