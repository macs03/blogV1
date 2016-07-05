from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', 'posts.views.post_list', name='postList'),
    url(r'^create/$', 'posts.views.post_create', name='postCreate'),
    url(r'^detail/$', 'posts.views.post_detail', name='postDetail'),
    url(r'^update/$', 'posts.views.post_update', name='postUpdate'),
    url(r'^delete/$', 'posts.views.post_delete', name='postDelete'),
)
