# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20160629_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creature_received', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reveived', to='main_app.Creature')),
                ('creature_sent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent', to='main_app.Creature')),
                ('user_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='main_app.User')),
                ('user_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='main_app.User')),
            ],
        ),
    ]