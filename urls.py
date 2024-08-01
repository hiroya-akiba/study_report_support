from django.urls import path
from . import views

app_name = 'srs'
urlpatterns = [
    path('', views.index, name='index'),
]