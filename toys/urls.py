from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_toys, name='toys'),
    path('<int:toy_id>/', views.toy_detail, name='toy_detail'),
]
