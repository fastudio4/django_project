# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:34
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20170519_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description_article',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]
