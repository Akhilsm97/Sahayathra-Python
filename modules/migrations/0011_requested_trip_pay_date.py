# Generated by Django 3.2.5 on 2023-05-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0010_requested_trip_trip_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested_trip',
            name='pay_date',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
    ]