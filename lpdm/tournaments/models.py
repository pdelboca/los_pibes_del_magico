from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tournament(models.Model):
	date = models.DateField()
	players = models.ManyToManyField(User)

	def __str__(self):
		return "Tournament {0}".format(self.date)

class Round(models.Model):
	tournament = models.OneToOneField(Tournament)
	round_number = models.IntegerField(default=0)

	def __str__(self):
		return "Round: {0} - {1}".format(self.round_number, self.tournament)


class Player(models.Model):
	user = models.OneToOneField(User)
	is_lta = models.BooleanField("Is LTA?")
	last_lta = models.DateField("Last LTA", blank=True, null=True)
	ltas = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class Match(models.Model):
	tournament = models.ForeignKey(Tournament, null=True)
	player_one = models.OneToOneField(Player, related_name="player_one")
	player_two = models.OneToOneField(Player, related_name="player_two")
	victories_player_one = models.IntegerField(default=0)
	victories_player_two = models.IntegerField(default=0)
	winner = models.OneToOneField(Player, related_name="winner")

	def ganador(self):
		if self.victories_player_one > self.victories_player_two:
			return self.player_one
		else:
			return self.player_two

	def __str__(self):
		return "{0}:{1} - {2}:{3}".format(self.Player_uno, self.victories_player_one,
		 self.player_two, self.victories_player_two)