# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 06:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator])),
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.CharField(max_length=200, unique=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='razorapp.Payee')),
            ],
        ),
    ]