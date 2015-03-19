from django.conf.urls import patterns, include, url
from django.contrib import admin

from base_communicator.views import main_page_view, home_page_view, register_view, login_view, logout_view, create_journey, add_note, journey_view, new_journey_view
from base_communicator.functions import register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Journey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page_view, name='main'),
    url(r'^home$', home_page_view, name='home'),
    url(r'^register/$', register_view, name='register'),
    url(r'^new_journey/$', new_journey_view, name='new_journey'),
    url(r'^create_journey/$', create_journey, name='create_journey'),
    url(r'^journey/(?P<journey_id>\w+)/$', journey_view, name='journey'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout')
)
