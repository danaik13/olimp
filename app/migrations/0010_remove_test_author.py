# Generated by Django 2.0.3 on 2018-04-09 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180409_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='author',
        ),
    ]
