# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneos', '0002_auto_20151130_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='torneo',
            field=models.ForeignKey(to='torneos.Torneo', null=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha',
            field=models.DateField(),
        ),
    ]
