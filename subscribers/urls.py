from django.conf.urls import url
from subscribers import views

urlpatterns = [
    url(r'^$', views.subscriber_list, name='subscriber_list'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^unsubscribe/(?P<email>[^/]+)/$', views.unsubscribe, name='unsubscribe'),
]
