from django.contrib.auth.models import User
from tournaments.models import Tournament, Match, Player
from datetime import datetime, timedelta

u1 = User(username="Chancha", password="Chancha")
u1.save()
u2 = User(username="Leo", password="Leo")
u2.save()
u3 = User(username="Ithan", password="Ithan")
u3.save()
u4 = User(username="Lari", password="Lari")
u4.save()
u5 = User(username="Tato", password="Tato")
u5.save()
u6 = User(username="Lucas", password="Lucas")
u6.save()
u7 = User(username="Pato", password="Pato")
u7.save()
u8 = User(username="Pop", password="Pop")
u8.save()
u9 = User(username="Jere", password="Jere")
u9.save()

p1 = Player(user=u1, is_lta=True, last_lta=datetime.now(), ltas=1)
p1.save()
p2 = Player(user=u2, is_lta=False, last_lta=None, ltas=0)
p2.save()
p3 = Player(user=u3, is_lta=False, last_lta=None, ltas=0)
p3.save()
p4 = Player(user=u4, is_lta=True, last_lta=datetime.now() - timedelta(days=7), 
	ltas=1)
p4.save()
p5 = Player(user=u5, is_lta=True, last_lta=datetime.now() - timedelta(days=15), 
	ltas=1)
p5.save()
p6 = Player(user=u6, is_lta=True, last_lta=datetime.now() - timedelta(days=15), 
	ltas=1)
p6.save()
p7 = Player(user=u7, is_lta=False, last_lta=None, ltas=0)
p7.save()
p8 = Player(user=u8, is_lta=False, last_lta=None, ltas=0)
p8.save()
p9 = Player(user=u9, is_lta=False, last_lta=None, ltas=0)
p9.save()


t1 = Tournament(date=datetime.now(), rounds=4)
t1.save()
t1.players.set([p1,p2,p3,p4,p5,p6,p7,p8,p9])