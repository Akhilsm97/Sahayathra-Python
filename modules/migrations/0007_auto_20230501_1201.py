# Generated by Django 3.2.5 on 2023-05-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_auto_20230501_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requested_trip',
            old_name='giver_reg',
            new_name='date',
        ),
        migrations.AddField(
            model_name='requested_trip',
            name='giver_name',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requested_trip',
            name='trip_id',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requested_trip',
            name='trip_status',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requested_trip',
            name='veh_model',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]