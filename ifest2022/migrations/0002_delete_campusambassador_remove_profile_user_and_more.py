# Generated by Django 4.1 on 2022-08-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifest2022', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='campusAmbassador',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='userProfile',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
