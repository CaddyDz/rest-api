# Generated by Django 3.0.3 on 2020-02-14 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phone_number',
            new_name='room_number',
        ),
    ]
