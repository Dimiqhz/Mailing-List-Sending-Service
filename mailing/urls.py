from django.conf.urls import url
from mailing import views

urlpatterns = [
    url(r'^create/$', views.create_campaign, name='create_campaign'),
    url(r'^list/$', views.campaign_list, name='campaign_list'),
    url(r'^logs/$', views.email_logs, name='email_logs'),
    url(r'^tracking/(?P<campaign_id>\d+)/(?P<subscriber_email>[^/]+)/$', views.tracking_pixel, name='tracking_pixel'),
]
