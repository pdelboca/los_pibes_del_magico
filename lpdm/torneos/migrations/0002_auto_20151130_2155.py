# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneo',
            name='partidos',
        ),
        migrations.AddField(
            model_name='partido',
            name='torneo',
            field=models.OneToOneField(null=True, to='torneos.Torneo'),
        ),
    ]
