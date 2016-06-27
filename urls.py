from django.conf.urls import patterns, include, url
from app import views


urlpatterns = patterns('',
    url(r'^GetResult/$', views.get_result, name='get_result'),
    url(r'^AddURLToQueue/$', views.add_url_to_queue, name='add_url_to_queue'),
)
