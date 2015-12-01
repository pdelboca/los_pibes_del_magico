from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from random import shuffle

from .models import Tournament


def index(request):
    tournament_list = Tournament.objects.order_by('-date')
    context = {'tournament_list': tournament_list}
    return render(request, 'tournaments/index.html', context)


def draft_positions(request, tournament_id):
    players_list = list(Tournament.objects.get(pk=tournament_id).players.all())
    shuffle(players_list)
    context = {'players_list': players_list}
    return render(request, 'tournaments/draft_positions.html', context)
