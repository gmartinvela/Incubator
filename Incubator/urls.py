from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Incubator.views.home', name='home'),
    url(r'^measures$', 'Incubator.views.measures', name='measures'),
    url(r'^lights/(?P<light_number>\w+)/(?P<command>\w+)/$', 'Incubator.views.lights', name='lights')
    # url(r'^Incubator/', include('Incubator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
