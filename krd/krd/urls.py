from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portfolio.views.index', name="home"),
    url(r'^(\w+)$', 'portfolio.views.project_page', name="project"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
