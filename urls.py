from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^login_rend/$', 'apps.common.view.login_rend'),
    #(r'^account/', include('apps.account.urls', namespace='account', app_name='account')),
    #(r'^auth/', include('apps.auth.urls', namespace='auth', app_name='auth')),
    #(r'^log/', include('apps.log.urls', namespace='log', app_name='log')),
    #(r'^dns_detection/', include('apps.dns_detection.urls', namespace='dns_detection', app_name='dns_detection')),
    #(r'^http_detection/', include('apps.http_detection.urls', namespace='http_detection', app_name='http_detection')),
    #(r'^monitor/', include('apps.monitor.urls', namespace='monitor', app_name='monitor')),
    (r'^product/', include('apps.product.urls', namespace='product', app_name='product')),
    (r'^supplier/', include('apps.supplier.urls', namespace='supplier', app_name='supplier')),
    (r'^common/', include('apps.common.urls', namespace='common', app_name='common')),
    (r'^order/', include('apps.order.urls', namespace='order', app_name='order')),
    (r'^ink/', include('apps.ink.urls', namespace='ink', app_name='ink')),
    (r'^$', 'django.contrib.auth.views.login', {'template_name':'index.html'}),
    (r'^safe/$','apps.common.views.common.about_safe'),
    (r'^index$','apps.common.views.common.index'),
    (r'^login/$', 'apps.common.views.common.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'index.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)

urlpatterns += staticfiles_urlpatterns()

