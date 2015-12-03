# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='tournament',
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=None, to='tournaments.Tournament'),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament_round',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='rounds',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Round',
        ),
    ]
