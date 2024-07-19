
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('get_weather.urls')),
    path('admin/', admin.site.urls),
]
