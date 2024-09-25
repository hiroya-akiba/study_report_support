from django.urls import path
from django.contrib import admin

from . import views

app_name = 'srs'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',
        views.ReportListview.as_view(),
        name='index'),

    path('report/<pk>/',
        views.ReportDetailView.as_view(),
        name='detail_report'),

    path('create_report/',
        views.ReportCreateView.as_view(),
        name='create_report'),

    path('create_subject/',
        views.SubjectCreateView.as_view(),
        name='create_subject'),
]