from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tournaments/
    url(r'^$', views.index, name='index'),
    # ex: /tournaments/5/draft_positions/
    url(r'^(?P<tournament_id>[0-9]+)/draft_positions/$', 
    	views.draft_positions, name='draft_positions'),
    # ex: /tournaments/5/detail/
    url(r'^(?P<tournament_id>[0-9]+)/detail/$', 
    	views.detail, name='detail'),
    # ex: /tournaments/5/current_round/
    url(r'^(?P<tournament_id>[0-9]+)/sort_next_round/$', 
    	views.sort_next_round, name='sort_next_round'),
]