# Generated by Django 3.2.5 on 2023-04-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_make_trips_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='make_trips',
            name='bal_seat',
            field=models.CharField(default='nul', max_length=20),
            preserve_default=False,
        ),
    ]
