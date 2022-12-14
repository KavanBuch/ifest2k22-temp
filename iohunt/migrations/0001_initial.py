# Generated by Django 4.1 on 2022-08-24 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('link', models.CharField(max_length=256, null=True, unique=True)),
                ('Data', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'NotStarted'), ('S', 'Started'), ('E', 'Ended')], default='N', max_length=1)),
                ('startTime', models.DateTimeField(null=True)),
                ('endTime', models.DateTimeField(null=True)),
                ('userProfile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
