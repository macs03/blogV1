from django.conf.urls import patterns, url
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

urlpatterns = [
    url(r'^$', post_list, name='postList'),
    url(r'^create/$', post_create, name='postCreate'),
    url(r'^(?P<id>\d+)/$', post_detail, name='postDetail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='postUpdate'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='postDelete'),
]
