# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:52
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20170531_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=ckeditor.fields.RichTextField(verbose_name='Comment'),
        ),
    ]