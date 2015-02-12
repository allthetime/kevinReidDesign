# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150127_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='pic',
            field=models.ImageField(default=b'/static/pics/no-img.jpg', upload_to=b'pics'),
            preserve_default=True,
        ),
    ]
