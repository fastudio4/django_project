# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 12:39
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20170529_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='description_article',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]