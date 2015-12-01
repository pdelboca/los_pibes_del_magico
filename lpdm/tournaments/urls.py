from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tournaments/
    url(r'^$', views.index, name='index'),
    # ex: /tournaments/5/posicion_draft/
    #url(r'^(?P<tournament_id>[0-9]+)/draft_position/$', 
    #	views.draft_position, name='draft_position'),
]