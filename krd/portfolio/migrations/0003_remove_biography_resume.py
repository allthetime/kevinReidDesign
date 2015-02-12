# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150127_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='resume',
        ),
    ]
