from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#admin.site.index_template = "admin/myindex.html"

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snowflake.views.home', name='home'),
    # url(r'^snowflake/', include('snowflake.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    'snowflake.views',
    url(r'^$', 'index', name="index"),
    url(r'^login/', 'login', name="login"),
)

urlpatterns += patterns(
    'receipt.views',
    url(r'^receipt_regist/', 'receipt_regist', name="receipt_regist"),
)
