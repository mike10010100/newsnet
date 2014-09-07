# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20140907_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='choice_text',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=2000),
        ),
    ]
