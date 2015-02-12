from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'portfolio.views.index', name="home"),
    url(r'^(\w+)$', 'portfolio.views.project', name="project"),
    url(r'^admin/', include(admin.site.urls), name='admin'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
