from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_toys, name='toys'),
    path('<toy_id>', views.toys_detail, name='toy_detail'),
]
