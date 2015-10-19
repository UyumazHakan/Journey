from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

import base_communicator.views.user_views as user
import base_communicator.views.journey_views as journey
import base_communicator.views.main_views as main
import base_communicator.views.friend_views as friend


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Journey.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', main.main_page_view, name='main'),
                       url(r'^home$', main.home_page_view, name='home'),
                       url(r'^search$', main.search_page_view, name='search'),
                       url(r'^(?P<user_id>[^/]+)/followers$', friend.follower_page_view, name='follower'),
                       url(r'^(?P<user_id>[^/]+)/followings', friend.following_page_view, name='following'),
                       url(r'^requests', friend.requests_page_view, name='requests'),
                       url(r'^register/$', user.register_view, name='register'),
                       url(r'^edit_profile/$', user.edit_profile_view, name='edit_profile'),
                       url(r'^edit_profile/post/$', user.post_edit_profile, name='post_edit_profile'),
                       url(r'^new_journey/$', journey.new_journey_view, name='new_journey'),
                       url(r'^create_journey/$', journey.create_journey, name='create_journey'),
                       url(r'^my_journeys/$', journey.accessible_journeys, name='accessible_journeys'),
                       url(r'^newsfeed/$', main.newsfeed_page_view, name='newsfeed'),
                       url(r'^journey/(?P<journey_id>\w+)/$', journey.journey_view, name='journey'),
                       url(r'^journey/(?P<journey_id>\w+)/love/$', journey.love_journey, name='love_journey'),
                       url(r'^journey/(?P<journey_id>\w+)/share/$', journey.share_journey, name='share_journey'),
                       url(r'^journey/(?P<journey_id>\w+)/add_note/$', journey.add_note, name='add_note'),
                       url(r'^journey/(?P<journey_id>\w+)/create_note/$', journey.create_note, name='create_note'),
                       url(r'^journey/(?P<journey_id>\w+)/add_note/$', journey.add_image, name='add_image'),
                       url(r'^journey/(?P<journey_id>\w+)/create_image/$', journey.create_image, name='create_image'),
                       url(r'^journey/(?P<journey_id>\w+)/add_comment/$', journey.add_comment, name='add_comment'),
                       url(r'^journey/(?P<journey_id>\w+)/create_comment/$', journey.create_comment,
                           name='create_comment'),
                       url(r'^activation/(?P<activation_key>\w+)/$', user.activate_view, name='activation'),
                       url(r'^login/$', user.login_view, name='login'),
                       url(r'^logout/$', user.logout_view, name='logout')
)
