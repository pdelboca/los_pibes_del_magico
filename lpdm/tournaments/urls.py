from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tournaments/
    url(r'^$', views.index, name='index'),
    # ex: /tournaments/5/draft_positions/
    url(r'^(?P<tournament_id>[0-9]+)/draft_positions/$', 
    	views.draft_position, name='draft_positions'),
]