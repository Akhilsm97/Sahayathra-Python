# Generated by Django 3.2.5 on 2023-05-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_auto_20230502_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested_trip',
            name='trip_id',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]