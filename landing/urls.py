from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('tempview', views.tempview, name='tempview')
]
