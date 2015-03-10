from django.conf.urls import patterns, include, url
from django.contrib import admin

from base_communicator.views import main_page_view, register_view, login_view, logout_view
from base_communicator.functions import register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Journey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page_view, name='main'),
    url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout')
)
