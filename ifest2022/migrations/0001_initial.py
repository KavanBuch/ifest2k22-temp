# Generated by Django 4.1 on 2022-08-24 14:13

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
            name='campusAmbassador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('rounds', models.PositiveIntegerField(null=True)),
                ('paid', models.BooleanField(null=True)),
                ('registrationDeadline', models.DateTimeField(null=True)),
                ('logo', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('Data', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ifest2022.event')),
                ('userProfile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=50, null=True)),
                ('payment', models.BooleanField(null=True)),
                ('contact_number', models.CharField(max_length=12, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('ieee_id', models.CharField(blank=True, max_length=10, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=12, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]