# Generated by Django 3.2.5 on 2023-05-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_make_trips_bal_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='requested_trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taker_name', models.CharField(max_length=20)),
                ('giver_reg', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='taker_reg',
            old_name='giver_name',
            new_name='taker_name',
        ),
        migrations.AddField(
            model_name='make_trips',
            name='trip_id',
            field=models.CharField(default='nul', max_length=20),
            preserve_default=False,
        ),
    ]
