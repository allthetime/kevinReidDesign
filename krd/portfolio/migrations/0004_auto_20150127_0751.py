# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_biography_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='resume',
            field=models.FileField(default='', upload_to=b'pdf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=b'/static/pics/no-img.jpg', upload_to=b'pics'),
            preserve_default=True,
        ),
    ]
