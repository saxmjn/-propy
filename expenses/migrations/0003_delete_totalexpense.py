# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_totalexpense'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TotalExpense',
        ),
    ]
