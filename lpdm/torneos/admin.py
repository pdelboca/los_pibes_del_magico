from django.contrib import admin
from .models import Torneo, Jugador, Partido

# Register your models here.
class PartidoInline(admin.TabularInline):
	model = Partido
	extra = 1

class TorneoAdmin(admin.ModelAdmin):
	inlines = [PartidoInline]


admin.site.register(Torneo, TorneoAdmin)
admin.site.register(Jugador)