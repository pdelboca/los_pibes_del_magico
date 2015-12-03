from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from random import shuffle

from .models import Tournament, Match

def home(request):
    return HttpResponseRedirect(reverse('tournaments:index'))    

def index(request):
    tournament_list = Tournament.objects.order_by('-date')
    context = {'tournament_list': tournament_list}
    return render(request, 'tournaments/index.html', context)


def detail(request, tournament_id):
    tournament = get_object_or_404(Tournament,pk=tournament_id)
    context = {'tournament': tournament}
    return render(request, 'tournaments/detail.html', context)


def draft_positions(request, tournament_id):
    players_list = list(Tournament.objects.get(pk=tournament_id).players.all())
    shuffle(players_list)
    context = {'players_list': players_list}
    return render(request, 'tournaments/draft_positions.html', context)

def sort_next_round(request, tournament_id):
    """
    Given a Tournament id, it creates all the matches for next round.
    If number of players is odd, one is going to be left without match.
    """
    tournament = get_object_or_404(Tournament,pk=tournament_id)
    current_round = tournament.current_round + 1
    players = tournament.players.all()
    players_id = list(players.values_list("id", flat=True))
    shuffle(players_id)
    matches = []

    # TODO: Move this logic to Tournament Class
    if current_round == 1:
        while len(players_id) > 1:
            m = Match()
            m.player_one = players.get(id=players_id.pop())
            m.player_two = players.get(id=players_id.pop())
            m.tournament = tournament
            m.tournament_round = current_round
            # m.save() For now, matches are going to be created on django-admin
            matches.append(m)
    else:
        pass

    if len(players_id) == 1:
        free_player = players.get(id=players_id.pop())
        free_player.bye_times = free_player.bye_times + 1
        # free_player.save()
    else:
        free_player = None

    tournament.current_round = current_round
    # tournament.save()
    context = {'tournament': tournament, 'current_round':current_round, 
                'matches':matches, 'free_player':free_player}
    return render(request, 'tournaments/current_round.html',context)