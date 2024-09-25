from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'srs'
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',
        views.ReportListview.as_view(),
        name='index'),
        
]