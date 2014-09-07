# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='question',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='question_text',
            new_name='post_text',
        ),
    ]
