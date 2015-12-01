from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Torneo(models.Model):
	fecha = models.DateField()
	jugadores = models.ManyToManyField(User)

	def __str__(self):
		return "Torneo del {0}".format(self.fecha)


class Jugador(models.Model):
	user = models.OneToOneField(User)
	is_lta = models.BooleanField("Es LTA?")
	ultimo_lta = models.DateField("Ultimo LTA", blank=True, null=True)
	ltas = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class Partido(models.Model):
	torneo = models.ForeignKey(Torneo, null=True)
	jugador_uno = models.OneToOneField(Jugador, related_name="jugador_uno")
	jugador_dos = models.OneToOneField(Jugador, related_name="jugador_dos")
	victorias_jugador_uno = models.IntegerField(default=0)
	victorias_jugador_dos = models.IntegerField(default=0)

	def ganador(self):
		if self.victorias_jugador_uno > self.victorias_jugador_dos:
			return self.jugador_uno
		else:
			return self.jugador_dos

	def __str__(self):
		return "{0}:{1} - {2}:{3}".format(self.jugador_uno, self.victorias_jugador_uno,
		 self.jugador_dos, self.victorias_jugador_dos)