from django.conf.urls import patterns, include, url
from django.contrib import admin

import base_communicator.views.user_views as user
import base_communicator.views.journey_views as journey
import base_communicator.views.main_views as main


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Journey.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', main.main_page_view, name='main'),
                       url(r'^home$', main.home_page_view, name='home'),
                       url(r'^register/$', user.register_view, name='register'),
                       url(r'^new_journey/$', journey.new_journey_view, name='new_journey'),
                       url(r'^create_journey/$', journey.create_journey, name='create_journey'),
                       url(r'^journey/(?P<journey_id>\w+)/$', journey.journey_view, name='journey'),
                       url(r'^journey/(?P<journey_id>\w+)/note_add/$', journey.add_note, name='add_note'),
                       url(r'^activation/(?P<activation_key>\w+)/$', user.activate_view, name='activation'),
                       url(r'^login/$', user.login_view, name='login'),
                       url(r'^logout/$', user.logout_view, name='logout')
)
