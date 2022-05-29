from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'), 
    path('detect/', views.detection, name='call'),
    path('eyedetect/', views.eyedetect, name='eyecall'),
]