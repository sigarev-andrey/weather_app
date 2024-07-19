from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),]