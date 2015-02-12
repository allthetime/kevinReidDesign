# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_biography_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='pic',
            field=models.ImageField(default=b'pics/no-img.jpg', upload_to=b'pics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=b'pics/no-img.jpg', upload_to=b'pics'),
            preserve_default=True,
        ),
    ]
