# Generated by Django 4.0.3 on 2022-03-25 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtotag',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventtotag',
            old_name='tag_id',
            new_name='tag',
        ),
    ]