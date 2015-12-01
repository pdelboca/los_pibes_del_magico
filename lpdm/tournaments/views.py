from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


from .models import Tournament


def index(request):
    tournament_list = Tournament.objects.order_by('-date')
    context = {'tournament_list': tournament_list}
    return render(request, 'tournaments/index.html', context)


def draft_position(request):
    pass
