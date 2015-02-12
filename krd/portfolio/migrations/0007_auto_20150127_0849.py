# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20150127_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='front_page',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default=b'pics/no-img.jpg', upload_to=b'pics'),
            preserve_default=True,
        ),
    ]
