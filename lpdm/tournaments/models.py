"""
Inspired: https://github.com/jcdenton/chess-tournament/tree/master/tournament
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
	user = models.OneToOneField(User)
	is_lta = models.BooleanField("Is LTA?")
	last_lta = models.DateField("Last LTA", blank=True, null=True)
	ltas = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username


class Tournament(models.Model):
	date = models.DateField()
	players = models.ManyToManyField(User)
	rounds = models.IntegerField(default=1)


	def __str__(self):
		return "Tournament {0}".format(self.date)

class Match(models.Model):
	RESULT_CHOICES = (
        ('1', 'Player 1 Wins!'),
        ('2', 'Player 2 Wins!'),
        ('3', 'Draw!'),
        ('4', 'Pending!')
    )
	tournament = models.ForeignKey(Tournament, default=None)
	tournament_round = models.IntegerField(default=1)
	player_one = models.OneToOneField(Player, related_name="player_one")
	player_two = models.OneToOneField(Player, related_name="player_two")
	victories_player_one = models.IntegerField(default=0)
	victories_player_two = models.IntegerField(default=0)
	winner = models.OneToOneField(Player, related_name="winner")
	result = models.CharField(max_length=1, default=4, choices=RESULT_CHOICES)
	finished = models.BooleanField()
	def __str__(self):
		return "{0}:{1} - {2}:{3}".format(self.Player_uno, self.victories_player_one,
		 self.player_two, self.victories_player_two)
