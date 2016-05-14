from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import APIRoot, CreateLogView


urlpatterns = patterns(
    '',
    url(r'^$', APIRoot.as_view(), name='api-root'),
    url(r'^log/$', CreateLogView.as_view(), name='log-create'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
