from django.contrib import admin
from .models import Tournament, Player, Match

# Register your models here.
class MatchInline(admin.TabularInline):
	model = Match
	extra = 1

class TournamentAdmin(admin.ModelAdmin):
	inlines = [MatchInline]
	filter_horizontal = ('players',)


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player)