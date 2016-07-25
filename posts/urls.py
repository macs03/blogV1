from django.conf.urls import patterns, url
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

urlpatterns = patterns('',
    url(r'^$', post_list, name='postList'),
    url(r'^create/$', post_create, name='postCreate'),
    url(r'^(?P<id>\d+)/$', post_detail, name='postDetail'),
    url(r'^update/$', post_update, name='postUpdate'),
    url(r'^delete/$', post_delete, name='postDelete'),
)
