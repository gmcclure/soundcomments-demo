from django.conf import settings
from django.conf.urls.defaults import patterns, include #, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'storyview.views.index'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^comment_form/(?P<story_id>.*)/(?P<block_id>.*)/$', 'storycomments.views.comment_form'),
    (r'^story_comments/(?P<story_id>.*)/$', 'storycomments.views.get_page_comments_as_json'),
    (r'^_/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    (r'^admin/', include(admin.site.urls)),
)
