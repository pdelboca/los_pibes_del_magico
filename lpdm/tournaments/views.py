from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from random import shuffle

from .models import Tournament

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
