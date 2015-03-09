from django.conf.urls import patterns, include, url
from django.contrib import admin

from web.views import main_page_view
from base_communicator.functions import register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Journey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page_view, name='main'),
    url(r'^register/$', register, name='register')
)
