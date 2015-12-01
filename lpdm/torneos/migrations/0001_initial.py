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
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_lta', models.BooleanField(verbose_name=b'Es LTA?')),
                ('ultimo_lta', models.DateField(verbose_name=b'Ultimo LTA')),
                ('ltas', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('victorias_jugador_uno', models.IntegerField(default=0)),
                ('victorias_jugador_dos', models.IntegerField(default=0)),
                ('jugador_dos', models.OneToOneField(related_name='jugador_dos', to='torneos.Jugador')),
                ('jugador_uno', models.OneToOneField(related_name='jugador_uno', to='torneos.Jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('partidos', models.ManyToManyField(to='torneos.Partido')),
            ],
        ),
    ]
