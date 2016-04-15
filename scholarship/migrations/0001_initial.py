# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('end_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('amount_type', models.CharField(max_length=60)),
                ('about', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]