"""footballrankings URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from players import views

urlpatterns = [
    url(r'^status/', views.statusAPI ,name='status'),
    url(r'^status2/', views.status2API ,name='status2'),
    url(r'^players/', views.PlayersInfoHtml.as_view() ,name='players'),
    url(r'^search/(?P<search_key>[\w\ ]+)', views.SearchInfoHtml.as_view() ,name='search'),
    url(r'^filters/(?P<filter_key>[\w\ ]+)', views.PlayersFilteredInfoHtml.as_view() ,name='filteredData'),
    url(r'^player/(?P<name>[\w\ ]+)', views.PlayerInfoHtml.as_view() ,name='player'),
    url(r'^players/json/', views.PlayersInfo.as_view() ,name='players2'),
    url(r'^player2/(?P<name>\w+)/json', views.PlayerInfo.as_view() ,name='player2'),

    url(r'^admin/', include(admin.site.urls)),
]