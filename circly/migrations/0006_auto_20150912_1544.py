# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circly', '0005_auto_20150912_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_email',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_phone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
