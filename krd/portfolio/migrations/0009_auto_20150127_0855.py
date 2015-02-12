# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20150127_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='path',
        ),
    ]
