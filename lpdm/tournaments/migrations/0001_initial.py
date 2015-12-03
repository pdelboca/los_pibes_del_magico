# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('victories_player_one', models.IntegerField(default=0)),
                ('victories_player_two', models.IntegerField(default=0)),
                ('result', models.CharField(default=4, max_length=1, choices=[(b'1', b'Player 1 Wins!'), (b'2', b'Player 2 Wins!'), (b'3', b'Draw!'), (b'4', b'Pending!')])),
                ('finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_lta', models.BooleanField(verbose_name=b'Is LTA?')),
                ('last_lta', models.DateField(null=True, verbose_name=b'Last LTA', blank=True)),
                ('ltas', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_number', models.IntegerField(default=0)),
                ('finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('rounds', models.IntegerField(default=0)),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.OneToOneField(to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='player_one',
            field=models.OneToOneField(related_name='player_one', to='tournaments.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player_two',
            field=models.OneToOneField(related_name='player_two', to='tournaments.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament_round',
            field=models.OneToOneField(to='tournaments.Round'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.OneToOneField(related_name='winner', to='tournaments.Player'),
        ),
    ]
