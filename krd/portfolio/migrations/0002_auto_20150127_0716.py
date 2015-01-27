# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bio', models.TextField(default=b'')),
                ('resume', models.FileField(upload_to=b'/static/pdf')),
                ('email', models.EmailField(default=b'', max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='front_page',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=b'/static/pics/no-img.jpg', upload_to=b'/static/pics'),
            preserve_default=True,
        ),
    ]
