from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from devices import views, device_customization_views

urlpatterns = [
    url(r'^devices\/?$', views.device_list),
    url(r'^devices\/(?P<pk>[0-9]+)\/?$', views.device_detail),
    url(r'^device_customs\/?$', device_customization_views.dc_list),
    url(r'^device_customs\/(?P<pk>[0-9]+)\/?$', device_customization_views.dc_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
