from django.conf.urls import url
from mailing import views

urlpatterns = [
    url(r'^create/$', views.create_mailing, name='create_mailing'),
    url(r'^tracking/(?P<campaign_id>\d+)/(?P<subscriber_email>[^/]+)/$', views.tracking_pixel, name='tracking_pixel'),
]
