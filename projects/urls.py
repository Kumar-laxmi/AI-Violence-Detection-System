from django.urls import path
from projects import views

urlpatterns = [
    path('', views.Home, name='Home'),
]