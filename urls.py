from django.urls import path
from . import views

app_name = 'srs'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_report/', views.create, name='createReport'),
    path('create_subject/', views.create, name='createSubject')
]