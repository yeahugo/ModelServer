# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='image_url',
            field=models.ImageField(upload_to=b'toys'),
        ),
        migrations.AlterField(
            model_name='model',
            name='thumbnail_url',
            field=models.ImageField(upload_to=b'toys'),
        ),
    ]
