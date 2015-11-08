# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meanings',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('meaning', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='VocabTables',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('table_title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('last_modified', models.DateTimeField(verbose_name='last modified')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('word', models.CharField(max_length=500)),
                ('vocabTable', models.ForeignKey(to='vocabulary.VocabTables')),
            ],
        ),
        migrations.AddField(
            model_name='meanings',
            name='word',
            field=models.ForeignKey(to='vocabulary.Words'),
        ),
    ]
