from django.conf.urls import url
from subscribers import views

urlpatterns = [
    url(r'^$', views.subscriber_list, name='subscriber_list'),
]
