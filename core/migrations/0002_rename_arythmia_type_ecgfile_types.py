# Generated by Django 3.2.4 on 2021-07-07 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecgfile',
            old_name='arythmia_type',
            new_name='types',
        ),
    ]
